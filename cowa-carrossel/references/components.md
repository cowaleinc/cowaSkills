# Component Reference

## Logo Lockup

```html
<!-- With logo icon -->
<div style="display:flex;align-items:center;gap:12px;">
  <div style="width:40px;height:40px;border-radius:50%;background:{BRAND_PRIMARY};display:flex;align-items:center;justify-content:center;">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
      <!-- icon paths -->
    </svg>
  </div>
  <span style="font-size:13px;font-weight:600;letter-spacing:0.5px;color:{DARK_BG};">{BRAND_NAME}</span>
</div>

<!-- With initials -->
<div style="display:flex;align-items:center;gap:12px;">
  <div style="width:40px;height:40px;border-radius:50%;background:{BRAND_PRIMARY};display:flex;align-items:center;justify-content:center;">
    <span style="font-size:18px;font-weight:600;color:#fff;">{FIRST_LETTER}</span>
  </div>
  <span style="font-size:13px;font-weight:600;letter-spacing:0.5px;color:{DARK_BG};">{BRAND_NAME}</span>
</div>
```

## Strikethrough Pills

```html
<span style="font-size:11px;padding:5px 12px;border:1px solid rgba(255,255,255,0.1);border-radius:20px;color:#6B6560;text-decoration:line-through;">
  {Old tool}
</span>
```

## Tag Pills

```html
<span style="font-size:11px;padding:5px 12px;background:rgba(255,255,255,0.06);border-radius:20px;color:{BRAND_LIGHT};">
  {Label}
</span>
```

## Prompt/Quote Box

```html
<div style="padding:16px;background:rgba(0,0,0,0.15);border-radius:12px;border:1px solid rgba(255,255,255,0.08);">
  <p style="font-size:13px;color:rgba(255,255,255,0.5);margin-bottom:6px;">{Label}</p>
  <p style="font-size:15px;color:#fff;font-style:italic;line-height:1.4;">"{Quote text}"</p>
</div>
```

## Color Swatches

```html
<div style="display:flex;gap:8px;">
  <div style="width:32px;height:32px;border-radius:8px;background:{color};border:1px solid rgba(255,255,255,0.08);"></div>
  <!-- repeat for more swatches -->
</div>
```

## CTA Button

```html
<div style="display:inline-flex;align-items:center;gap:8px;padding:12px 28px;background:{LIGHT_BG};color:{BRAND_DARK};font-weight:600;font-size:14px;border-radius:28px;">
  {CTA TEXT}
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M5 12h14M12 5l7 7-7 7"/>
  </svg>
</div>
```

## Instagram Frame Chrome

```html
<!-- Header -->
<div style="display:flex;align-items:center;gap:10px;padding:12px 16px;">
  <div style="width:32px;height:32px;border-radius:50%;background:{BRAND_PRIMARY};"></div>
  <div>
    <span style="font-size:14px;font-weight:600;">@{handle}</span>
    <span style="font-size:12px;color:#888;display:block;">{subtitle}</span>
  </div>
</div>

<!-- Actions -->
<div style="display:flex;gap:16px;padding:8px 16px;">
  <!-- Heart, Comment, Share, Bookmark SVG icons -->
</div>

<!-- Caption -->
<div style="padding:12px 16px;">
  <span style="font-size:14px;"><strong>@{handle}</strong> {caption}</span>
  <span style="font-size:12px;color:#888;display:block;margin-top:4px;">2 HOURS AGO</span>
</div>
```
