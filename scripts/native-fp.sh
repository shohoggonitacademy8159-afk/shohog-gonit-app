#!/usr/bin/env bash
# নেটিভ অংশের আঙুলছাপ: android/ ফাইল, capacitor.config আর নেটিভ প্লাগইনের সংস্করণ।
# এটা না বদলালে নতুন সংস্করণ APK ছাড়াই (অ্যাপের ভেতর থেকে এক চাপে) বসানো যায়।
cd "$(dirname "$0")/.."
{ git ls-files -s android capacitor.config.json
  node -e "const l=require('./package-lock.json').packages;for(const k of Object.keys(l).sort())if(/^node_modules\/@(capacitor|capgo)\//.test(k))console.log(k,l[k].version)"
} | sha256sum | cut -c1-12
