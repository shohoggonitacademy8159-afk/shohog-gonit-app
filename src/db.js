// সহগ গণিত একাডেমি — Firebase সংযোগ (Firestore + অ্যাডমিন লগইন)
// window.SohogDB নামে অ্যাপকে একটি ছোট ইন্টারফেস দেয়।
import { initializeApp } from 'firebase/app';
import {
  initializeFirestore, persistentLocalCache, persistentMultipleTabManager,
  collection, doc, setDoc, getDoc, getDocFromServer, deleteDoc, onSnapshot, query, orderBy
} from 'firebase/firestore';
import {
  getAuth, onAuthStateChanged, signInWithEmailAndPassword, signOut,
  setPersistence, browserLocalPersistence
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
  checkAdmin() {
    return getDocFromServer(doc(fs, 'admin', 'check')).then(() => true, () => false);
  },
  onAuth(cb) { return onAuthStateChanged(auth, u => cb(u ? { email: (u.email || '').toLowerCase() } : null)); },
  signIn(email, password) { return signInWithEmailAndPassword(auth, email, password).catch(e => { const x = new Error('auth'); x.code = (e && e.code) || 'auth/unknown'; throw x; }); },
  signOut() { return signOut(auth); }
};
