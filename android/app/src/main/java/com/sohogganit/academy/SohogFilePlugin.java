package com.sohogganit.academy;

import android.content.Intent;
import android.net.Uri;
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
}
