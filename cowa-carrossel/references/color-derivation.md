# Color Derivation Reference

## From Primary to Full Palette

Given a single brand primary color, derive the complete palette:

```javascript
function derivePalette(hexColor) {
  // hexColor: "#3B82F6" (example: blue)

  const rgb = hexToRgb(hexColor);
  // { r: 59, g: 130, b: 246 }

  // BRAND_LIGHT: lighten ~20%
  const brandLight = lighten(rgb, 0.20);
  // "#60A5FA"

  // BRAND_DARK: darken ~30%
  const brandDark = darken(rgb, 0.30);
  // "#1E40AF"

  // LIGHT_BG: warm/cool off-white
  const lightBg = isWarm(rgb) ? "#FEF7ED" : "#F8FAFC";
  // Based on whether primary skews warm or cool

  // LIGHT_BORDER: slightly darker than LIGHT_BG
  const lightBorder = darken(lightBg, 0.05);

  // DARK_BG: near-black with brand tint
  const darkBg = isWarm(rgb) ? "#1A1918" : "#0F172A";

  return {
    BRAND_PRIMARY: hexColor,
    BRAND_LIGHT: rgbToHex(brandLight),
    BRAND_DARK: rgbToHex(brandDark),
    LIGHT_BG: lightBg,
    LIGHT_BORDER: lightBorder,
    DARK_BG: darkBg
  };
}
```

## Temperature Detection

```javascript
function isWarm(rgb) {
  // Determine if color is warm (red/orange/yellow) or cool (blue/green/purple)
  const { r, g, b } = rgb;
  // Simple heuristic: more red = warmer
  const warmth = r - (g + b) / 2;
  return warmth > 20;
}
```

## Warm vs Cool Palettes

| Temperature | LIGHT_BG | DARK_BG |
|-------------|----------|---------|
| Warm | #FEF7ED (warm cream) | #1A1918 (warm black) |
| Cool | #F8FAFC (cool gray-white) | #0F172A (slate dark) |

## Common Brand Colors

| Color Name | Hex | Warm/Cool | Best For |
|-----------|-----|-----------|----------|
| Coral | #FF6B6B | Warm | Food, Lifestyle, Wellness |
| Navy | #1E3A8A | Cool | Finance, Tech, Professional |
| Forest | #166534 | Neutral | Nature, Sustainability |
| Purple | #7C3AED | Cool | Creative, Wellness, Luxury |
| Terracotta | #DC2626 | Warm | Fashion, Home, Artisan |
| Teal | #0D9488 | Cool | Health, Tech, Modern |
