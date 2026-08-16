# How to Change Colors, Gradients, Strokes, and Opacity in a Telemetry Template

The Template Editor in Shred Scopes provides styling controls for text, shapes, telemetry graphics, ticks, images, and nested templates. The exact controls depend on the selected layer, but the general workflow is to choose a layer, edit its visible paint and outline, then check the result against several frames of the source footage.

This tutorial explains how to make those changes without altering the telemetry mapping or motion of the layer.

## Open a template for editing

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and load a source with telemetry. Open the Template Editor and choose the template to restyle.

When starting with a built-in template, use "Template" > "Save As New" before making extensive changes. This creates a custom copy and preserves the original design.

## Understand the three kinds of transparency

Several controls can make a layer appear transparent, but they do not have the same effect:

- A transparent fill removes or fades the interior paint while leaving the stroke and other effects available.
- A transparent stroke removes or fades the outline while leaving the fill available.
- Layer opacity fades the complete layer, including its fill, stroke, text, image content, shadow, and glow.

Use paint transparency when one part of the style should remain solid. Use layer opacity when the entire element should fade uniformly.

## 1. Select the exact layer to change

Select an element on the canvas or choose it in "Layers." Confirm the layer name and type before changing its style.

Common layer-specific controls include:

- Text, arc text, and data text: font, fill, stroke, stroke width, spacing, alignment, and shadow
- Shapes and graphic paths: fill, stroke, line width, line caps, line joins, and dash patterns
- Data graphics: paints for a track, progress region, pointer, marker, chart, or other visible part
- Data ticks: separate styles for major ticks, minor ticks, labels, and guide lines
- Images and nested templates: whole-layer opacity, blend mode, and other layer-level effects

If the expected control is not shown, select the visible child layer that draws that part of the design. Styling options vary by layer type.

## 2. Change a solid color

Open the relevant "Fill," "Stroke," or component paint control and choose a solid paint. Select the color, then preview it on the canvas.

For a simple high-contrast overlay, use a small, consistent palette:

- One primary color for important values
- One neutral color for labels and outlines
- One background or shadow color that separates the graphic from the footage
- One warning or highlight color when a telemetry condition requires it

Avoid using several nearly identical colors for elements that need to be distinguished quickly.

## 3. Create a gradient

Where the layer offers gradient paint, choose a linear or radial gradient instead of a solid color.

A linear gradient changes color along a direction. Use its stops and direction to control where each color appears. A radial gradient changes outward from a center point and is useful for circular gauges, soft highlights, and background discs.

After creating the gradient:

1. Keep the number of stops limited unless the design requires a complex transition.
2. Check that adjacent colors remain distinguishable over the source footage.
3. Review the gradient at the intended export size.
4. Confirm that important text or pointers do not sit over the least legible part of the gradient.

Some data-driven layers also offer signed or range-based paints. A signed paint can use different colors for positive and negative values. A range paint can change color as the value crosses configured ranges. These are data-dependent styles rather than fixed gradients, so preview both the low and high parts of the telemetry timeline.

## 4. Configure a stroke

A stroke outlines text, shapes, paths, and supported graphic components. Choose the stroke paint, then set its width.

Where available, also review:

- Stroke alignment, which places the line inside, across, or outside the edge
- Line cap, which controls the ends of open paths
- Line join, which controls how connected segments meet
- Dash settings, which create broken or patterned lines

For data text, a modest dark stroke around light text often remains readable across more footage than an unoutlined value. Excessively thick strokes can close the counters inside small letters and numbers, so check digits such as 0, 6, 8, and 9 at normal playback size.

## 5. Adjust layer opacity

Use "Opacity" to fade the complete selected layer. A lower value allows more of the layers or source footage below to show through.

Opacity is useful for background plates, secondary labels, route fills, and decorative elements. Keep primary telemetry values sufficiently opaque to remain readable while the source scene changes.

Opacity and blend mode interact. If a partially transparent layer changes unexpectedly after a blend mode is selected, return the blend mode to its normal default, judge the opacity first, and then test the blend mode again.

## 6. Add separation with a shadow or glow

Supported layers can include shadow or glow controls. Choose a contrasting color and adjust opacity, blur, distance, and angle where available.

A short, soft dark shadow can separate light text from bright sky, snow, or water. A glow can help a line or pointer stand out, but a large blur can make precise telemetry graphics appear soft. Use effects as supporting contrast rather than as the only source of readability.

## 7. Check every independently styled part

Complex layers can have multiple visible components. For example, a gauge may contain a track, progress arc, pointer, central value, and tick labels. Changing one paint does not necessarily change the others.

Move through the layer controls and verify that:

- Related components use coordinated colors.
- Text and numeric values have sufficient contrast.
- Positive, negative, and range colors mean what their labels imply.
- Major and minor ticks remain visually distinct.
- Decorative layers do not compete with changing telemetry.

Template constants can centralize colors and fonts that must remain synchronized across several compatible controls.

## 8. Preview against representative footage

Play the preview and inspect frames containing both bright and dark scenery. Scrub to fast motion, complex backgrounds, and the minimum and maximum values used by the graphic.

If the template will be placed over footage in Source Composite, perform the final readability check there. A style that looks clear on the Template Editor's transparent canvas can behave differently over the actual video.

Also check the intended export resolution. Fine strokes, small type, and subtle transparency can look acceptable while editing but become difficult to read after downscaling.

## 9. Save the custom style

Use "Save" for an existing custom template or "Template" > "Save As New" for a new version. Give the saved template a name that identifies the style or intended footage.

The custom template now retains its layer colors, gradients, strokes, effects, and opacity settings for later Shred Scopes projects.
