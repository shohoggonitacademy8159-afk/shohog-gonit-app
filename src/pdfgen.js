// কাস্টম প্রশ্নপত্র PDF: অ্যাপের ভেতরে তৈরি পাতাগুলো (A4, 794×1123 px) ছবি করে PDF বানায় — বাংলা যুক্তাক্ষর ও গণিত লেখা অ্যাপের মতোই থাকে।
// প্রয়োজনে আলাদা ফাইল (www/pdfgen.js) হিসেবে লোড হয়, তাই অ্যাপ খোলা ধীর হয় না।
import html2canvas from 'html2canvas-pro';
import { jsPDF } from 'jspdf';
import { Capacitor } from '@capacitor/core';
import { Filesystem, Directory } from '@capacitor/filesystem';
import { Share } from '@capacitor/share';

window.SohogPDF = {
  async render(pages, onProgress) {
    const pdf = new jsPDF({ unit: 'pt', format: 'a4', compress: true });
    for (let i = 0; i < pages.length; i++) {
      const cv = await html2canvas(pages[i], { scale: 2, backgroundColor: '#ffffff', logging: false, useCORS: true });
      if (i) pdf.addPage();
      pdf.addImage(cv.toDataURL('image/jpeg', 0.88), 'JPEG', 0, 0, 595.28, 841.89, undefined, 'FAST');
      if (onProgress) onProgress(i + 1, pages.length);
    }
    return pdf;
  },
  async save(pdf, name) {
    if (Capacitor.isNativePlatform()) {
      const data = pdf.output('datauristring').split(',')[1];
      const safe = name.replace(/[^\wঀ-৿ .-]+/g, ' ').trim() || 'prosnopotro.pdf';
      const r = await Filesystem.writeFile({ path: safe, data, directory: Directory.Cache });
      await Share.share({ title: safe, url: r.uri, dialogTitle: 'PDF সংরক্ষণ বা শেয়ার করুন' });
      return 'shared';
    }
    pdf.save(name);
    return 'downloaded';
  }
};
