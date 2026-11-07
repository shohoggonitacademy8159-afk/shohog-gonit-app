// সহগ গণিত একাডেমি — Firebase সংযোগ (Firestore + অ্যাডমিন লগইন)
// window.SohogDB নামে অ্যাপকে একটি ছোট ইন্টারফেস দেয়।
import { initializeApp } from 'firebase/app';
import {
  initializeFirestore, persistentLocalCache, persistentMultipleTabManager,
  collection, doc, setDoc, getDoc, getDocFromServer, deleteDoc, onSnapshot, query, orderBy
} from 'firebase/firestore';
import {
  getAuth, onAuthStateChanged, signInWithEmailAndPassword, signOut,
  setPersistence, browserLocalPersistence, createUserWithEmailAndPassword,
  sendPasswordResetEmail, updateProfile
} from 'firebase/auth';

let fs = null, auth = null;

function code(e) {
  const c = (e && e.code) || '';
  if (c.includes('permission-denied')) return 'permission_denied';
  if (c.includes('unavailable')) return 'unavailable';
  return c || 'unknown';
}
function wrapErr(e) { const x = new Error((e && e.message) || 'error'); x.code = code(e); x.raw = e && e.code; return x; }

function colRef(name) {
  let order = null;
  const api = {
    orderBy(field) { order = field; return api; },
    onSnapshot(next, onErr) {
      const base = collection(fs, name);
      const q = order ? query(base, orderBy(order)) : base;
      return onSnapshot(q, snap => {
        next({ docs: snap.docs.map(d => ({ id: d.id, data: () => d.data() })) });
      }, e => onErr && onErr(wrapErr(e)));
    },
    doc(id) {
      const r = doc(fs, name, id);
      return {
        get: () => getDoc(r).then(x => (x.exists() ? x.data() : null), e => { throw wrapErr(e); }),
        set: data => setDoc(r, data).catch(e => { throw wrapErr(e); }),
        delete: () => deleteDoc(r).catch(e => { throw wrapErr(e); })
      };
    }
  };
  return api;
}

window.SohogDB = {
  init(config) {
    if (!config || !config.apiKey || String(config.apiKey).startsWith('PASTE')) return false;
    const app = initializeApp(config);
    try {
      fs = initializeFirestore(app, { localCache: persistentLocalCache({ tabManager: persistentMultipleTabManager() }) });
    } catch (e) {
      fs = initializeFirestore(app, {});
    }
    auth = getAuth(app);
    setPersistence(auth, browserLocalPersistence).catch(() => {});
    return true;
  },
  collection: colRef,
  // সার্ভারের নিয়ম অনুযায়ী অ্যাডমিন কিনা যাচাই (admin/check পড়ার অনুমতি শুধু অ্যাডমিনের)
  // true = অ্যাডমিন, false = অ্যাডমিন নয়, null = এখন যাচাই করা যাচ্ছে না (ইন্টারনেট নেই)
  checkAdmin() {
    return getDocFromServer(doc(fs, 'admin', 'check')).then(() => true, e => (code(e) === 'permission_denied' ? false : null));
  },
  onAuth(cb) { return onAuthStateChanged(auth, u => cb(u ? { uid: u.uid, email: (u.email || '').toLowerCase(), name: u.displayName || '' } : null)); },
  signIn(email, password) {
    return signInWithEmailAndPassword(auth, email, password)
      .then(c => ({ uid: c.user.uid, email: (c.user.email || '').toLowerCase() }))
      .catch(e => { const x = new Error('auth'); x.code = (e && e.code) || 'auth/unknown'; throw x; });
  },
  // শিক্ষার্থীর নতুন অ্যাকাউন্ট (ইমেইল/পাসওয়ার্ড; শুধু ফোন হলে ফোন থেকে বানানো ইমেইল)
  signUp(email, password, name) {
    return createUserWithEmailAndPassword(auth, email, password)
      .then(c => (name ? updateProfile(c.user, { displayName: name }).catch(() => {}) : null).then(() => ({ uid: c.user.uid, email: (c.user.email || '').toLowerCase() })))
      .catch(e => { const x = new Error('auth'); x.code = (e && e.code) || 'auth/unknown'; throw x; });
  },
  resetPassword(email) {
    return sendPasswordResetEmail(auth, email).catch(e => { const x = new Error('auth'); x.code = (e && e.code) || 'auth/unknown'; throw x; });
  },
  signOut() { return signOut(auth); },
  // একটি ডকুমেন্ট পড়া/লেখা/নজর রাখা (শিক্ষার্থীর অ্যাকাউন্ট ও ফোন নম্বরের জন্য)
  docGet(col, id) { return getDocFromServer(doc(fs, col, id)).then(x => (x.exists() ? x.data() : null), e => { throw wrapErr(e); }); },
  docSet(col, id, data, merge) { return setDoc(doc(fs, col, id), data, merge ? { merge: true } : {}).catch(e => { throw wrapErr(e); }); },
  docWatch(col, id, next, onErr) { return onSnapshot(doc(fs, col, id), x => next(x.exists() ? x.data() : null), e => onErr && onErr(wrapErr(e))); }
};

// ফোনের লোকাল নোটিফিকেশন (সার্ভার ছাড়া) — শুধু অ্যান্ড্রয়েড অ্যাপে কাজ করে, ওয়েবে চুপচাপ কিছুই করে না
import { Capacitor } from '@capacitor/core';
import { LocalNotifications } from '@capacitor/local-notifications';
window.SohogNotify = {
  native: Capacitor.isNativePlatform(),
  async ready() {
    if (!this.native) return false;
    try {
      let p = await LocalNotifications.checkPermissions();
      if (p.display === 'prompt' || p.display === 'prompt-with-rationale') p = await LocalNotifications.requestPermissions();
      if (p.display !== 'granted') return false;
      if (!this._ch) {
        this._ch = true;
        await LocalNotifications.createChannel({ id: 'exam', name: 'পরীক্ষার খবর', importance: 4, visibility: 1, vibration: true }).catch(() => {});
        await LocalNotifications.createChannel({ id: 'admin', name: 'অ্যাডমিন: পেমেন্ট ও রিপোর্ট', importance: 4, visibility: 1, vibration: true }).catch(() => {});
      }
      return true;
    } catch (e) { return false; }
  },
  // list: [{id, title, body, at (ms, optional), channel}]
  async schedule(list) {
    if (!list.length || !(await this.ready())) return false;
    try {
      await LocalNotifications.schedule({
        notifications: list.map(n => ({
          id: n.id, title: n.title, body: n.body, channelId: n.channel || 'exam',
          largeBody: n.body, schedule: n.at ? { at: new Date(n.at), allowWhileIdle: true } : undefined,
          extra: n.extra || null
        }))
      });
      return true;
    } catch (e) { return false; }
  },
  async pendingIds() {
    if (!this.native) return [];
    try { const r = await LocalNotifications.getPending(); return (r.notifications || []).map(n => n.id); } catch (e) { return []; }
  },
  async cancel(ids) {
    if (!this.native || !ids.length) return;
    try { await LocalNotifications.cancel({ notifications: ids.map(id => ({ id })) }); } catch (e) {}
  },
  onTap(cb) {
    if (!this.native) return;
    LocalNotifications.addListener('localNotificationActionPerformed', a => { try { cb((a && a.notification && a.notification.extra) || {}); } catch (e) {} });
  }
};
