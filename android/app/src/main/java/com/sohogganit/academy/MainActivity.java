package com.sohogganit.academy;

import android.os.Bundle;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // ফলাফল ফাইল (CSV) সংরক্ষণ/শেয়ারের জন্য অ্যাপের নিজস্ব প্লাগইন
        registerPlugin(SohogFilePlugin.class);
        super.onCreate(savedInstanceState);
    }
}
