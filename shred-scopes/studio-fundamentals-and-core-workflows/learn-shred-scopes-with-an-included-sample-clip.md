# How to Learn Shred Scopes with an Included Sample Clip

Shred Scopes includes sample GoPro clips that can be loaded directly in Studio. A sample provides footage and prepared telemetry for learning the Template Editor, testing built-in designs, and comparing overlay readability without selecting a personal video.

Use a sample to learn the controls. Use an original GoPro clip before making final decisions about data availability, timing, aspect ratio, placement, or export settings for personal footage.

## Open the sample picker

1. Open [Shred Scopes](https://shredscopes.com/) on a desktop computer.
2. Sign in and select "Studio" from the navigation.
3. At the source picker, select "Use Sample Clip."
4. Review the available sample cards.
5. Select the sample that suits the type of preview needed.

The current sample set includes:

- "Sunny Ski Run," which provides bright snow and strong sunlight for checking a graphic against a high-glare scene.
- "Snowstorm Ski Run," which provides gray skies and falling snow for checking contrast in a lower-visibility scene.

After a selection, wait for Studio to load the footage and telemetry. The "Choose Template" step appears when the sample is ready.

## Choose a template to inspect

Start with a built-in template so the first session focuses on the workspace rather than constructing a design.

Useful starting points include:

- A speed template for observing changing numeric and gauge values
- An altitude or terrain-profile template for reviewing a chart across time
- A GPS path template for seeing a route build through the selected range
- A heading template for observing directional change
- A grade or G-force template for inspecting signed or rapidly changing values

Choose a design whose visual style is easy to distinguish from the sample background. Imperial and metric versions are available for many measured templates.

The [public template catalog](https://shredscopes.com/gopro-telemetry-overlay-templates) can be used to compare current built-in designs before selecting one in Studio.

## Practice preview and timeline controls

After the template opens, use the bottom bar to review its animation:

1. Select "Play preview" or press Space.
2. Pause at a point where the data changes clearly.
3. Drag the playhead to another part of the clip.
4. Use the preview zoom options to inspect the canvas at a comfortable size.
5. Move the playhead near the beginning and end to check the template's range.

When the timeline has focus, Left and Right move the playhead by five frames. Shift+Left and Shift+Right perform a finer one-frame nudge.

Preview zoom affects only the on-screen workspace. It does not change the template canvas or export resolution.

## Practice Template Editor actions

The sample telemetry can drive changes immediately, making it useful for learning how layers respond.

Try the following non-destructive exercises:

- Select a text or data-graphic layer from the layer list.
- Move the selected layer on the canvas.
- Change its color, stroke, or opacity.
- Change a compatible unit conversion.
- Hide and show the layer with its visibility control.
- Lock the layer and confirm that direct canvas movement is prevented.
- Use undo and redo to review the changes.
- Open another template in a separate tab and compare it at the same point in the sample.

Built-in originals are not overwritten. Use "Save As New" only when the altered design should be retained as a custom template.

## Practice Source Composite

Select "Composite Mode" or press `M` to view the template over the sample footage.

In Source Composite, practice:

- Selecting a preset or custom output canvas
- Switching the source between "Cover" and "Contain"
- Moving and scaling the overlay
- Locking the source or template after placement
- Adding another telemetry template
- Setting timeline in and out points
- Previewing the source and graphics together

Use "Template Editor Mode" or press `M` to return to the individual template. The Source Composite arrangement remains available while moving between these views.

## Compare the two sample environments

The samples can be used as a simple readability test.

On the bright sample, inspect whether light text, thin strokes, or low-opacity shapes disappear against snow. On the darker, lower-contrast sample, inspect whether muted colors or transparent backgrounds make values difficult to distinguish.

Possible adjustments include:

- Adding or strengthening a text stroke
- Placing a semi-opaque shape behind a value
- Increasing contrast between the foreground and background
- Moving the graphic away from a visually busy area
- Increasing the size of small text or tick marks

No single sample represents every recording condition. A design intended for reuse should also be checked against the actual footage before export.

## Start over with another sample

To clear the active source and templates, resolve any work that should be saved and select "Reset" in the top toolbar. Confirm the reset to return Studio to its startup state, then select "Use Sample Clip" again.

The top-toolbar reset clears the active Studio project. The separate reset control inside Source Composite restores framing values but does not return to the source picker.

## What a sample does not establish

A successful sample session confirms that the editor and selected design can be explored in the current browser. It does not confirm that another file contains the same telemetry.

An original GoPro clip can differ in:

- Available GPS and motion streams
- Duration and frame rate
- Resolution and aspect ratio
- Camera orientation
- Recorded route and value ranges
- Background brightness and visual complexity

After learning the controls, reset Studio, choose the original GoPro clip, and repeat the template preview with its actual telemetry before starting a final export.

