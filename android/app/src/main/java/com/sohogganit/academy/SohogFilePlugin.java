package com.sohogganit.academy;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.net.Uri;
import android.util.Base64;
import com.getcapacitor.JSArray;
import androidx.core.content.FileProvider;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;
import java.io.File;
import java.io.FileOutputStream;
import java.nio.charset.StandardCharsets;

/** লেখা (যেমন ফলাফলের CSV) একটি ফাইলে রেখে অ্যান্ড্রয়েডের শেয়ার/সংরক্ষণ তালিকা খোলে। কোনো অনুমতি লাগে না। */
@CapacitorPlugin(name = "SohogFile")
public class SohogFilePlugin extends Plugin {

    @PluginMethod
    public void share(PluginCall call) {
        String name = call.getString("name", "result.csv");
        String mime = call.getString("mime", "text/csv");
        String content = call.getString("content", "");
        String title = call.getString("title", "ফলাফল সংরক্ষণ বা শেয়ার");
        try {
            String safe = name.replaceAll("[^A-Za-z0-9._-]", "_");
            File dir = new File(getContext().getCacheDir(), "exports");
            if (!dir.exists() && !dir.mkdirs()) {
                call.reject("folder");
                return;
            }
            File file = new File(dir, safe);
            try (FileOutputStream out = new FileOutputStream(file)) {
                out.write(content.getBytes(StandardCharsets.UTF_8));
            }
            Uri uri = FileProvider.getUriForFile(getContext(), getContext().getPackageName() + ".fileprovider", file);
            Intent send = new Intent(Intent.ACTION_SEND);
            send.setType(mime);
            send.putExtra(Intent.EXTRA_STREAM, uri);
            send.putExtra(Intent.EXTRA_SUBJECT, safe);
            send.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
            Intent chooser = Intent.createChooser(send, title);
            chooser.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
            getActivity().startActivity(chooser);
            call.resolve();
        } catch (Exception e) {
            call.reject("share failed", e);
        }
    }

    /** অ্যাপে আপলোড করা PDF (base64 টুকরো) ফাইলে জোড়া দিয়ে ফোনের PDF রিডারে খোলে */
    @PluginMethod
    public void openPdf(PluginCall call) {
        String name = call.getString("name", "file.pdf");
        String title = call.getString("title", "PDF");
        JSArray parts = call.getArray("parts");
        if (parts == null || parts.length() == 0) {
            call.reject("empty");
            return;
        }
        try {
            String safe = name.replaceAll("[^A-Za-z0-9._-]", "_");
            if (!safe.toLowerCase().endsWith(".pdf")) safe = safe + ".pdf";
            File dir = new File(getContext().getCacheDir(), "exports");
            if (!dir.exists() && !dir.mkdirs()) {
                call.reject("folder");
                return;
            }
            File file = new File(dir, safe);
            try (FileOutputStream out = new FileOutputStream(file)) {
                for (int i = 0; i < parts.length(); i++) {
                    out.write(Base64.decode(parts.getString(i), Base64.DEFAULT));
                }
            }
            Uri uri = FileProvider.getUriForFile(getContext(), getContext().getPackageName() + ".fileprovider", file);
            Intent view = new Intent(Intent.ACTION_VIEW);
            view.setDataAndType(uri, "application/pdf");
            view.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
            Intent chooser = Intent.createChooser(view, title);
            chooser.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
            try {
                getActivity().startActivity(chooser);
            } catch (ActivityNotFoundException nf) {
                call.reject("noviewer");
                return;
            }
            call.resolve();
        } catch (Exception e) {
            call.reject("open failed", e);
        }
    }
}
