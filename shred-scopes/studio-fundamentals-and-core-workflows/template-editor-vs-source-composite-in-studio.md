# Template Editor vs Source Composite in Studio

Studio contains two connected editing views. The Template Editor controls the contents of an individual telemetry graphic. Source Composite controls how one or more of those graphics are arranged over the original GoPro video.

The distinction is based on what is being edited: the template itself or the final composition containing the source footage.

## View comparison

| Capability | Template Editor | Source Composite |
| --- | --- | --- |
| Edit layers inside a telemetry design | Yes | Open the selected overlay in a linked Template Editor tab |
| Change template canvas size | Yes | No; Source Composite changes the output-video canvas instead |
| Map a layer to telemetry | Yes | No; mapping belongs to the included template |
| Change text, colors, fonts, shapes, or data graphics | Yes | Use "Edit Template" to return to the template's internal controls |
| Position the source video | No | Yes |
| Arrange several templates over one source | No | Yes |
| Set Source Composite in and out points | No | Yes |
| Export a standalone overlay | Yes | No |
| Export a finished video with source audio | No | Yes |

## Template Editor

The Template Editor opens after a telemetry source and template are selected. It is the primary workspace for designing the overlay.

Use it to:

- Add or delete layers
- Change layer order
- Group, align, distribute, lock, hide, or duplicate elements
- Move, resize, and rotate supported layers
- Connect data text, graphics, and ticks to telemetry streams
- Convert units and configure data ranges
- Change colors, fills, strokes, opacity, blend modes, fonts, images, and other styles
- Resize the template canvas
- Preview animation against the active telemetry
- Save a custom template or separate copy
- Export the template as a standalone overlay

The left sidebar contains the source, export, constants, and layer controls. The top toolbar contains template tabs and actions. The canvas shows the active template, while the bottom bar contains status, zoom, playback, and the telemetry timeline.

## Source Composite

Source Composite opens when the original video is linked and "Composite Mode" is selected. It uses the current template as an overlay above the source footage.

Use it to:

- Choose the output-video canvas dimensions
- Fit the source with "Cover" or "Contain"
- Move, scale, align, lock, or rotate the source video
- Add one or more telemetry templates
- Move, scale, align, lock, duplicate, edit, or remove an overlay
- Set the export in and out points
- Rebuild range-dependent graphics for the selected segment
- Select H.264 or HEVC/H.265 where supported
- Set bitrate and advanced encoding controls
- Export a finished MP4 containing the source video, telemetry graphics, and source audio

Source Composite does not expose the internal controls of a selected overlay. Use "Edit Template" when its layers, data mapping, canvas, or appearance must change.

## Open the appropriate view

Open [Shred Scopes](https://shredscopes.com/), sign in, and select "Studio."

After loading a source and choosing a template, the Template Editor opens automatically. Select "Composite Mode" or press `M` to open Source Composite.

Select "Template Editor Mode" or press `M` again to return.

If "Composite Mode" is unavailable, verify that:

- The source video has finished loading.
- The original matching file is linked when saved telemetry was used.
- The source is not a GoPro `.360` video.

Saved telemetry can drive the Template Editor without an original video. Source Composite requires the source frames and audio, so it cannot proceed from telemetry alone.

## Edit an overlay from Source Composite

When a placed overlay needs changes:

1. Select the overlay in Source Composite.
2. Select "Edit Template."
3. Change its internal layers or settings in the linked Template Editor tab.
4. Preview the telemetry in that tab.
5. Return to Source Composite with "Composite Mode" or `M`.
6. Confirm the edited overlay against the source video.

The linked tab remains connected to the Source Composite arrangement. This allows the design to be revised without rebuilding its placement from the beginning.

## Understand the two canvas sizes

The Template Editor canvas defines the dimensions and coordinate system of the telemetry graphic itself.

The Source Composite canvas defines the dimensions of the finished video. A template can be scaled and positioned within that larger output canvas.

For example, a square telemetry template can be placed in the corner of a widescreen Source Composite. Resizing the Source Composite canvas changes the video output, while resizing the template canvas changes the graphic's internal design space.

Use "Resize" in Template Editor for the template canvas. Use a preset or "Custom Size" in Source Composite for the final video canvas.

## Understand the two reset controls

The top toolbar's "Reset" clears the active source and open workspaces and returns Studio to startup after unresolved changes are handled.

The reset control at the bottom of the Source Composite panel restores source and overlay framing values. It does not clear the project or return to the source picker.

Check which reset control is being selected before confirming an action.

## Choose the view by task

Use Template Editor when the task begins with one of these questions:

- Which telemetry stream should this element display?
- How should the gauge, text, path, or chart look?
- What unit should the value use?
- How should the layers be arranged inside the overlay?
- What should the standalone overlay export contain?

Use Source Composite when the task begins with one of these questions:

- Where should this overlay appear on the GoPro video?
- How should the source be cropped, fitted, or rotated?
- Which additional telemetry templates should be added?
- What segment of the source should be exported?
- What dimensions, codec, and bitrate should the finished MP4 use?

The views are complementary. Template Editor defines the graphic; Source Composite defines how that graphic and the GoPro source become one video.

