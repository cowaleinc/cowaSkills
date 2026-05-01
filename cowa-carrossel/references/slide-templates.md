# Slide Templates

## Slide 1: Hero (LIGHT_BG)

```html
<div style="width:420px;height:525px;background:{LIGHT_BG};display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:36px;position:relative;">
  <!-- Optional watermark logo at low opacity -->
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);opacity:0.04;">
    <svg width="300" height="300" viewBox="0 0 24 24" fill="{BRAND_PRIMARY}">
      <!-- watermark icon -->
    </svg>
  </div>

  <!-- Logo lockup -->
  <div style="margin-bottom:32px;">
    <div style="width:40px;height:40px;border-radius:50%;background:{BRAND_PRIMARY};display:inline-block;"></div>
  </div>

  <!-- Tag -->
  <span style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:{BRAND_PRIMARY};margin-bottom:16px;">{TAG}</span>

  <!-- Main headline -->
  <h1 style="font-size:32px;font-weight:600;line-height:1.1;color:{DARK_BG};margin:0 0 16px;">{Bold statement}</h1>

  <!-- Subheadline -->
  <p style="font-size:14px;color:#6B6560;max-width:320px;">{Supporting text}</p>

  {progress_bar}
  {swipe_arrow}
</div>
```

## Slide 2: Problem (DARK_BG)

```html
<div style="width:420px;height:525px;background:{DARK_BG};display:flex;flex-direction:column;justify-content:center;padding:36px;position:relative;">
  <span style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:{BRAND_LIGHT};margin-bottom:16px;">{TAG}</span>

  <h2 style="font-size:28px;font-weight:600;line-height:1.15;color:#fff;margin:0 0 24px;">{Pain point headline}</h2>

  <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px;">
    <!-- Strikethrough pills -->
    <span style="font-size:11px;padding:5px 12px;border:1px solid rgba(255,255,255,0.1);border-radius:20px;color:#6B6560;text-decoration:line-through;">{Old tool 1}</span>
    <span style="font-size:11px;padding:5px 12px;border:1px solid rgba(255,255,255,0.1);border-radius:20px;color:#6B6560;text-decoration:line-through;">{Old tool 2}</span>
  </div>

  <p style="font-size:14px;color:rgba(255,255,255,0.6);max-width:340px;">{Problem description}</p>

  {progress_bar}
  {swipe_arrow}
</div>
```

## Slide 3: Solution (Brand Gradient)

```html
<div style="width:420px;height:525px;background:linear-gradient(165deg, {BRAND_DARK} 0%, {BRAND_PRIMARY} 50%, {BRAND_LIGHT} 100%);display:flex;flex-direction:column;justify-content:center;padding:36px;position:relative;">
  <span style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:rgba(255,255,255,0.6);margin-bottom:16px;">{TAG}</span>

  <h2 style="font-size:28px;font-weight:600;line-height:1.15;color:#fff;margin:0 0 20px;">{Solution headline}</h2>

  <p style="font-size:14px;color:rgba(255,255,255,0.8);max-width:340px;margin-bottom:24px;">{Solution description}</p>

  <!-- Optional quote box -->
  <div style="padding:16px;background:rgba(0,0,0,0.15);border-radius:12px;border:1px solid rgba(255,255,255,0.08);">
    <p style="font-size:13px;color:rgba(255,255,255,0.5);margin-bottom:6px;">{Label}</p>
    <p style="font-size:15px;color:#fff;font-style:italic;line-height:1.4;">"{Quote}"</p>
  </div>

  {progress_bar}
  {swipe_arrow}
</div>
```

## Slide 4: Features (LIGHT_BG)

```html
<div style="width:420px;height:525px;background:{LIGHT_BG};display:flex;flex-direction:column;padding:36px;padding-bottom:52px;position:relative;">
  <span style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:{BRAND_PRIMARY};margin-bottom:8px;">{TAG}</span>
  <h2 style="font-size:26px;font-weight:600;color:{DARK_BG};margin:0 0 16px;">{Features headline}</h2>

  <div style="flex:1;overflow:hidden;">
    <!-- Feature list -->
    <div style="display:flex;align-items:flex-start;gap:14px;padding:10px 0;border-bottom:1px solid {LIGHT_BORDER};">
      <span style="color:{BRAND_PRIMARY};font-size:15px;">{icon}</span>
      <div>
        <span style="font-size:14px;font-weight:600;color:{DARK_BG};display:block;">{Label}</span>
        <span style="font-size:12px;color:#8A8580;">{Description}</span>
      </div>
    </div>
    <!-- repeat for more features -->
  </div>

  {progress_bar}
  {swipe_arrow}
</div>
```

## Slide 5: Details (DARK_BG)

```html
<div style="width:420px;height:525px;background:{DARK_BG};display:flex;flex-direction:column;padding:36px;padding-bottom:52px;position:relative;">
  <span style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:{BRAND_LIGHT};margin-bottom:8px;">{TAG}</span>
  <h2 style="font-size:26px;font-weight:600;color:#fff;margin:0 0 20px;">{Details headline}</h2>

  <div style="flex:1;">
    <p style="font-size:14px;color:rgba(255,255,255,0.7);margin-bottom:16px;">{Description}</p>

    <!-- Color swatches or other visuals -->
    <div style="display:flex;gap:8px;margin-bottom:20px;">
      <div style="width:40px;height:40px;border-radius:8px;background:{color1};border:1px solid rgba(255,255,255,0.1);"></div>
      <div style="width:40px;height:40px;border-radius:8px;background:{color2};border:1px solid rgba(255,255,255,0.1);"></div>
    </div>

    <!-- Tag pills -->
    <div style="display:flex;flex-wrap:wrap;gap:8px;">
      <span style="font-size:11px;padding:5px 12px;background:rgba(255,255,255,0.06);border-radius:20px;color:{BRAND_LIGHT};">{Option 1}</span>
      <span style="font-size:11px;padding:5px 12px;background:rgba(255,255,255,0.06);border-radius:20px;color:{BRAND_LIGHT};">{Option 2}</span>
    </div>
  </div>

  {progress_bar}
  {swipe_arrow}
</div>
```

## Slide 6: How-to (LIGHT_BG)

```html
<div style="width:420px;height:525px;background:{LIGHT_BG};display:flex;flex-direction:column;padding:36px;padding-bottom:52px;position:relative;">
  <span style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:{BRAND_PRIMARY};margin-bottom:8px;">{TAG}</span>
  <h2 style="font-size:26px;font-weight:600;color:{DARK_BG};margin:0 0 16px;">{How-to headline}</h2>

  <div style="flex:1;overflow:hidden;">
    <!-- Numbered steps -->
    <div style="display:flex;align-items:flex-start;gap:16px;padding:14px 0;border-bottom:1px solid {LIGHT_BORDER};">
      <span style="font-size:26px;font-weight:300;color:{BRAND_PRIMARY};min-width:34px;line-height:1;">01</span>
      <div>
        <span style="font-size:14px;font-weight:600;color:{DARK_BG};display:block;">{Step title}</span>
        <span style="font-size:12px;color:#8A8580;">{Step description}</span>
      </div>
    </div>
    <!-- repeat for more steps -->
  </div>

  {progress_bar}
  {swipe_arrow}
</div>
```

## Slide 7: CTA (Brand Gradient) - NO SWIPE ARROW

```html
<div style="width:420px;height:525px;background:linear-gradient(165deg, {BRAND_DARK} 0%, {BRAND_PRIMARY} 50%, {BRAND_LIGHT} 100%);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:36px;position:relative;">
  <!-- Logo lockup -->
  <div style="margin-bottom:24px;">
    <div style="width:48px;height:48px;border-radius:50%;background:#fff;display:inline-flex;align-items:center;justify-content:center;">
      <span style="font-size:20px;font-weight:700;color:{BRAND_PRIMARY};">{INITIAL}</span>
    </div>
  </div>

  <h2 style="font-size:28px;font-weight:600;color:#fff;margin:0 0 12px;">{CTA headline}</h2>
  <p style="font-size:14px;color:rgba(255,255,255,0.8);margin-bottom:28px;">{Supporting text}</p>

  <!-- CTA Button -->
  <div style="display:inline-flex;align-items:center;gap:8px;padding:14px 32px;background:#fff;color:{BRAND_DARK};font-weight:600;font-size:14px;border-radius:28px;">
    {CTA TEXT}
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M5 12h14M12 5l7 7-7 7"/>
    </svg>
  </div>

  {progress_bar}
  <!-- NO swipe arrow on last slide -->
</div>
```
