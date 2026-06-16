# Branch 04 — Flexbox, Grid, and Responsive Layout

This branch is designed for Chapter 4 layout practice.

## Main idea

The HTML files are the same. The layout changes by switching the CSS file in the `<head>`.

In `index.html`, use this line for the Flexbox version:

```html
<link rel="stylesheet" href="layout-flex.css">
```

Or use this line for the Grid version:

```html
<link rel="stylesheet" href="layout-grid.css">
```

For `pages/contact.html`, remember that the file is inside a subfolder, so the path starts with `../`:

```html
<link rel="stylesheet" href="../layout-flex.css">
```

or:

```html
<link rel="stylesheet" href="../layout-grid.css">
```

## What students should notice

- Flexbox is useful for one-dimensional layouts: navbar rows, card rows, and alignment.
- Grid is useful for two-dimensional layouts: cards arranged in rows and columns.
- Media queries change the layout at different screen widths.
- The same HTML can be displayed in different layouts by changing only the stylesheet.

## Suggested Git branch name

```bash
git checkout -b ch4-flex-grid-layout
```

Then copy the files from this folder into the project root, commit, and push.
