---
name: cowa-carrossel
description: Crie carrosséis profissionais do Instagram com preview interativo. Ferramenta do CoWale Creative Suite para gerar conteúdo visual alinhado à marca. Use quando usuários pedem criar posts do Instagram, carrossel, gráficos para redes sociais. Gatilhos: "criar post Instagram", "fazer carrossel", "post carrossel", "cowa carrossel".
---

# Cowa Carrossel

A professional Instagram carousel generator from the CoWale Creative Suite. Create fully self-contained, swipeable HTML carousels where every slide is designed for Instagram export in brand-aware formats.

**Part of the CoWale ecosystem** — empowering businesses to build their legacy through strategic branding and digital ecosystems.

---

## About CoWale

CoWale is the strategic partner for traditional businesses delivering excellence in their services but losing ground due to outdated commercial processes. We bridge the gap between traditional business and the new economy.

**What we deliver:**
- **Branding**: Elevate brand perception, justify premium pricing, and build lasting legacy
- **Systems & Technology**: Automate lead attraction and sales funnels for predictable profit

Learn more: [cowaleinc](https://www.instagram.com/cowaleinc)

---

## Step 1: Collect Brand Details

Ask the user for (or derive from provided URL):

| Field | Required | Purpose |
|-------|----------|---------|
| Brand name | Yes | First and last slide |
| Instagram handle | Yes | Header and caption |
| Primary color | Yes | Generate full palette |
| Logo | No | SVG path, initial, or skip |
| Font preference | No | Editorial, modern, warm, etc. |
| Tone | No | Professional, casual, playful |
| Theme | Yes | What the carousel is about |

**If user says "make carousel about X" without details:** Ask before generating. Don't assume defaults.

**If URL provided:** Extract colors and style automatically.

## Step 2: Derive Color System

From one primary color, generate the full palette:

```
BRAND_PRIMARY = {user's color}
BRAND_LIGHT = {primary lightened ~20%}
BRAND_DARK = {primary darkened ~30%}
LIGHT_BG = {warm/cool off-white}
LIGHT_BORDER = {LIGHT_BG darkened ~5%}
DARK_BG = {near-black with brand tint}
```

**Rules:**
- Warm primary → warm cream bg; Cool primary → cool gray-white
- DARK_BG: warm → #1A1918, cool → #0F172A
- Brand gradient: `linear-gradient(165deg, BRAND_DARK 0%, BRAND_PRIMARY 50%, BRAND_LIGHT 100%)`

## Step 3: Typography

| Style | Heading Font | Body Font |
|-------|-------------|-----------|
| Editorial | Playfair Display | DM Sans |
| Modern | Plus Jakarta Sans | Plus Jakarta Sans |
| Warm | Lora | Nunito Sans |
| Technical | Space Grotesk | Space Grotesk |
| Bold | Fraunces | Outfit |

**Font scale:**
- Headings: 28-34px, 600, letter-spacing -0.3px
- Body: 14px, 400, line-height 1.5
- Tags: 10px, 600, letter-spacing 2px, uppercase
- Step numbers: 26px, 300

## Step 4: Build Carousel HTML

### Format
- Aspect ratio: 4:5 (Instagram standard)
- Each slide: 864×1134px content area (420px viewport scaled 2.57x for export)
- Alternate LIGHT_BG and DARK_BG for visual rhythm

### Required Elements (Every Slide)

**Progress Bar** (bottom):
```javascript
function progressBar(index, total, isLightSlide) {
  const pct = ((index + 1) / total) * 100;
  const track = isLightSlide ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.12)';
  const fill = isLightSlide ? BRAND_PRIMARY : '#fff';
  const label = isLightSlide ? 'rgba(0,0,0,0.3)' : 'rgba(255,255,255,0.4)';

  return `<div style="position:absolute;bottom:0;left:0;right:0;padding:16px 28px 20px;z-index:10;display:flex;align-items:center;gap:10px;">
    <div style="flex:1;height:3px;background:${track};border-radius:2px;overflow:hidden;">
      <div style="height:100%;width:${pct}%;background:${fill};border-radius:2px;"></div>
    </div>
    <span style="font-size:11px;color:${label};font-weight:500;">${index + 1}/${total}</span>
  </div>`;
}
```

**Swipe Arrow** (right edge, not on last slide):
```javascript
function swipeArrow(isLightSlide) {
  const bg = isLightSlide ? 'rgba(0,0,0,0.06)' : 'rgba(255,255,255,0.08)';
  const stroke = isLightSlide ? 'rgba(0,0,0,0.25)' : 'rgba(255,255,255,0.35)';

  return `<div style="position:absolute;right:0;top:0;bottom:0;width:48px;z-index:9;display:flex;align-items:center;justify-content:center;background:linear-gradient(to right,transparent,${bg});">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
      <path d="M9 6l6 6-6 6" stroke="${stroke}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>`;
}
```

## Step 5: Slide Sequence (7 slides ideal)

| # | Type | Background | Purpose |
|---|------|------------|---------|
| 1 | Hero | LIGHT_BG | Hook + logo lockup |
| 2 | Problem | DARK_BG | Pain point |
| 3 | Solution | Brand gradient | Answer |
| 4 | Features | LIGHT_BG | Feature list with icons |
| 5 | Details | DARK_BG | Specs, customization |
| 6 | How-to | LIGHT_BG | Numbered steps |
| 7 | CTA | Brand gradient | Call to action (no arrow) |

**Rules:**
- Lead with value proposition, not description
- Last slide: no swipe arrow, 100% progress bar
- Can flex: 5-10 slides based on content

## Step 6: Reusable Components

### Tag Label
```html
<span style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:2px;color:{COLOR};margin-bottom:16px;">{TAG}</span>
```

### Feature List
```html
<div style="display:flex;align-items:flex-start;gap:14px;padding:10px 0;border-bottom:1px solid {LIGHT_BORDER};">
  <span style="color:{BRAND_PRIMARY};font-size:15px;width:18px;">{icon}</span>
  <div>
    <span style="font-size:14px;font-weight:600;color:{DARK_BG};display:block;">{Label}</span>
    <span style="font-size:12px;color:#8A8580;">{Description}</span>
  </div>
</div>
```

### Numbered Steps
```html
<div style="display:flex;align-items:flex-start;gap:16px;padding:14px 0;border-bottom:1px solid {LIGHT_BORDER};">
  <span style="font-size:26px;font-weight:300;color:{BRAND_PRIMARY};min-width:34px;line-height:1;">{01}</span>
  <div>
    <span style="font-size:14px;font-weight:600;color:{DARK_BG};display:block;">{Title}</span>
    <span style="font-size:12px;color:#8A8580;">{Description}</span>
  </div>
</div>
```

### CTA Button (final slide only)
```html
<div style="display:inline-flex;align-items:center;gap:8px;padding:12px 28px;background:{LIGHT_BG};color:{BRAND_DARK};font-weight:600;font-size:14px;border-radius:28px;">
  {CTA TEXT}
</div>
```

## Step 7: Instagram Frame Wrapper

Wrap preview in Instagram-style frame:

- **Header:** Avatar (BRAND_PRIMARY circle) + handle + subtitle
- **Viewport:** 420×525px (4:5 ratio), swipeable track
- **Dots:** Dot indicators below viewport
- **Actions:** Heart, comment, share, bookmark icons
- **Caption:** Handle + description + timestamp

**Critical:** `.ig-frame` must be exactly **420px wide**. Export scales to 1080px via device_scale_factor.

## Step 8: Export as PNG

After user approval, export each slide as **1080×1350px PNG**:

```bash
python scripts/export_slides.py --input carousel.html --output slides/ --slides 7
```

**Critical rules:**
- Keep 420px layout width (device_scale_factor=2.5714 scales to 1080px)
- Embed images as base64
- Wait 3s for fonts to load
- Hide IG frame chrome before screenshot

## Output Files

The skill generates:
1. `carousel.html` - Interactive preview
2. `slides/slide_1.png` through `slide_N.png` - Export-ready images

---

## Credits

**Created by Gabriel Costa** ([eugabecosta](https://www.instagram.com/eugabecosta/))

### Gabriel Costa
- Website: [gabecosta.com](https://gabecosta.com/)
- Instagram: [@eugabecosta](https://www.instagram.com/eugabecosta/)
- Threads: [@eugabecosta](https://www.threads.com/@eugabecosta)
- YouTube: [@eugabecosta](https://www.youtube.com/@eugabecosta)
- LinkedIn: [in/eugabecosta](https://www.linkedin.com/in/eugabecosta/)
- GitHub: [eugabecosta](https://github.com/eugabecosta)

### CoWale
- Instagram: [@cowaleinc](https://www.instagram.com/cowaleinc)
- YouTube: [@cowaleinc](https://www.youtube.com/@cowaleinc)
- GitHub: [cowale](https://github.com/cowale)

---

## License

MIT License - See LICENSE file for details.