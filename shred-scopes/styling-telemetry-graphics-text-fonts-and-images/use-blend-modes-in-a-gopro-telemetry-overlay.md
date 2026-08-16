# How to Use Blend Modes in a GoPro Telemetry Overlay

A blend mode changes how a selected template layer combines with the visible content beneath it. This can make a layer darken, lighten, increase contrast, borrow color characteristics, or create a stylized difference effect.

Blend modes depend on the backdrop. The same overlay layer can look different over another template layer, a transparent canvas, or changing GoPro footage. They should therefore be chosen with representative source frames rather than from an isolated preview alone.

## Establish the layer order first

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the intended template in the Template Editor.

Review "Layers" before changing a blend mode. The selected layer blends with the content below it, so moving the layer can change the result even when every style setting remains the same.

For predictable testing:

1. Put the selected layer at its intended front-to-back position.
2. Set its opacity to fully visible.
3. Start with the normal default blend mode.
4. Preview the baseline appearance.
5. Test other modes one at a time.

## Understand common blend-mode groups

The available modes can be grouped by their general visual effect.

### Normal and replacement behavior

The default mode places the layer over those beneath it using its ordinary color and transparency.

"Copy" and "xor" can produce replacement or cutout-like results that differ sharply from normal layering. Use them only when that behavior is intentional, and inspect the complete canvas for areas that become unexpectedly transparent or replaced.

### Lightening modes

"Screen" generally lightens the combined result and can make bright marks or glow-like graphics interact with a darker backdrop. "Lighten" retains lighter contributions when comparing the layer with content beneath it. "Lighter" creates an additive result and can become very bright where colors overlap.

These modes can disappear over bright sky, snow, or reflective water, so test the brightest frames.

### Darkening modes

"Multiply" generally darkens the combined result. "Darken" retains darker contributions when comparing the layer with content below.

These can integrate shadows, textures, or dark graphic elements into a light background, but they can become difficult to see over forest, asphalt, night footage, or other dark scenes.

### Contrast modes

"Overlay," "hard-light," and "soft-light" combine lightening and darkening behavior to alter contrast. Soft light is usually more restrained, while hard light can create stronger transitions. The result depends heavily on both the selected layer and its backdrop.

Use these modes cautiously for numeric text and fine tick labels because changing footage can alter their apparent contrast from frame to frame.

### Color and tonal modes

"Hue," "saturation," "color," and "luminosity" combine selected color or brightness characteristics from the layer with those beneath it. They can be useful for controlled graphic treatments, but their result may be less obvious on grayscale or low-saturation content.

### Difference modes

"Difference" and "exclusion" create contrast according to differences between overlapping colors. They can produce a visible stylized result, but the hue can change continuously over moving footage.

"Color-dodge" and "color-burn" can create intense highlights or shadows. Test them for clipping, harsh transitions, and loss of detail.

## 1. Select the layer to blend

Select the intended text, shape, data graphic, ticks, image, group, or nested-template layer. Open "Blend mode" and choose a mode.

The blend applies to the selected layer as a rendered whole. If only one internal part of a complex graphic should blend, select that specific editable layer or component rather than applying the effect to a larger group.

## 2. Compare the mode with the default

Switch between the candidate and the default mode while viewing the same frame. Compare:

- Readability of numbers and labels
- Visibility of thin paths and ticks
- Color changes
- Transparency at the canvas edges
- Interaction with shadows, glows, and strokes
- Whether the layer still communicates its intended state

A visually interesting result is not useful if viewers can no longer read the telemetry.

## 3. Adjust opacity after choosing the mode

Once a blend mode is selected, use "Opacity" to control the strength of the complete layer. Reducing opacity mixes more of the backdrop into the result.

Do not use low opacity to correct a mode that fails entirely on part of the footage. Select a more stable mode, add a backing shape or stroke, or keep the default blend for critical information.

Fill opacity and layer opacity are different. A transparent fill can preserve a solid stroke, while layer opacity fades the stroke and effects as well.

## 4. Preview over actual GoPro footage

Place the template in Source Composite and scrub through frames containing:

- Bright sky, snow, sand, or water
- Dark forest, road, interior, or night scenes
- Highly saturated clothing, vehicles, or trail markers
- Fast motion and motion blur
- Detailed textures such as foliage or gravel

Check both the telemetry layer and the source detail beneath it. Some modes improve integration by allowing texture through, while others obscure the footage or make the overlay disappear.

## 5. Check changing telemetry states

For data-driven paint, preview positive and negative values, range changes, warning colors, and empty or unavailable states. A mode that works for a bright positive color may fail for a dark negative color.

If the layer contains several paints, evaluate each one against representative source frames. Add a neutral outline or background when the data color must change but readability must remain stable.

## 6. Consider the final export workflow

A standalone overlay can have transparency where no source exists beneath it. Its blend appearance in another video editor will depend on the footage and compositing behavior used there.

For a finished Source Composite video, the source footage is already part of the preview and output. Judge the blend mode in Source Composite before exporting.

When a transparent overlay will be used elsewhere, produce a short test and place it over the intended footage in the destination editor. Do not assume that the isolated transparent preview represents the final composite.

## 7. Restore predictable compositing when needed

Return "Blend mode" to the default if the layer changes too much across the video. The default is generally the most stable choice for primary numbers, unit labels, warning states, and other information that must stay readable.

Blend effects are more suitable for decorative elements, image treatments, soft backgrounds, and secondary graphics when their visibility is not the only way to interpret the telemetry.

## 8. Save and export a short test

Save the custom template, then export a short range that contains both bright and dark frames. Review the file at normal playback size and confirm that compression has not weakened thin or partially blended elements.

Keep the blend mode only when the layer remains intentional, legible, and consistent throughout the representative test.
