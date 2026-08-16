# Transparent Telemetry Overlay vs Source Composite: Which Shred Scopes Workflow Should You Use?

Shred Scopes can produce telemetry video in two principal ways. The Template Editor exports the telemetry graphic by itself, while Source Composite renders one or more telemetry templates directly over the original GoPro footage.

Both workflows use the same extracted telemetry and template system. The correct choice depends on where the graphics and source video should be combined.

## Comparison

| Consideration | Standalone telemetry overlay | Source Composite |
| --- | --- | --- |
| Output content | Telemetry graphics only | GoPro video, telemetry graphics, and source audio |
| Primary workspace | Template Editor | Source Compositor |
| Source video required at export | No, if saved telemetry is already loaded | Yes, the matching original video is required |
| Typical file types | PNG MOV, QuickTime Animation MOV, WebM, or keyed H.264 MP4 | H.264 or HEVC/H.265 MP4 |
| Transparency | Available with supported MOV and WebM formats | Not applicable because graphics are rendered over the source |
| Final placement | Completed in another video editor | Completed inside Shred Scopes |
| Multiple overlays over footage | Arranged later in another editor | Arranged together in Source Composite |
| Source audio | Not included | Included from the original video |
| GoPro `.360` source | Telemetry can drive an overlay | Video cannot currently be composited |

## Choose a standalone telemetry overlay when

Export the template by itself when the video will be finished in software such as Adobe Premiere Pro, DaVinci Resolve, Final Cut Pro, or another editor that supports the chosen overlay format.

This workflow is appropriate when:

- The GoPro footage still needs trimming, color work, stabilization, reframing, transitions, or other edits.
- Telemetry must be placed over several shots or integrated with other titles and graphics.
- A transparent background is required.
- The same overlay export will be used in more than one edit.
- Only saved telemetry is available and the original source does not need to appear in Shred Scopes.
- The finishing application will control the final canvas, audio, and delivery format.

Transparency-capable choices include PNG-codec MOV, QuickTime Animation MOV, and supported WebM configurations. H.264 MP4 can be used only with a solid background that is removed later with a chroma-key effect.

## Choose Source Composite when

Use Source Composite when the original GoPro video is already suitable for the intended output and the telemetry graphics can be positioned and rendered inside Shred Scopes.

This workflow is appropriate when:

- A finished MP4 is needed without using another video editor.
- The original source audio should be included automatically.
- One or more telemetry templates need to be positioned over the clip.
- Source fitting, rotation, scaling, and output dimensions can be completed in Studio.
- Only a selected segment of the source needs to be rendered.
- H.264 or HEVC/H.265 is an acceptable final codec.

Source Composite requires the original matching source file. Telemetry saved to an account contains data, but it does not contain the original video frames or audio.

## Shared preparation

The two workflows begin in the same way:

1. Open [Shred Scopes](https://shredscopes.com/), sign in, and select "Studio."
2. Choose an original GoPro clip, saved telemetry, or a sample clip.
3. Select a built-in or custom template.
4. Preview the template against the active telemetry.
5. Make any required changes to data, units, layout, text, color, or canvas size.

The decision occurs after the template is ready.

## Standalone-overlay workflow

Remain in the Template Editor and complete the following steps:

1. Select the overlay format.
2. Choose full, half, or quarter export size.
3. Enable source timecode when the selected format supports it and the edit requires it.
4. Select "Export."
5. Import the resulting file into the finishing application.
6. Place it on a video track above the corresponding GoPro footage.

The source clip and overlay must remain aligned. If one file is trimmed, retimed, or shifted independently, its displayed telemetry can cease to match the video.

## Source Composite workflow

From the Template Editor, select "Composite Mode" or press `M`, then:

1. Confirm that the matching original source video is linked.
2. Select an output canvas size.
3. Fit and position the source video.
4. Position the current template and add any additional templates.
5. Set the in and out points.
6. Rebuild range-dependent graphics if needed.
7. Choose the codec and video quality controls.
8. Review the compatibility result.
9. Select "Export" and save the finished MP4.

Source Composite preserves the arrangement when returning to Template Editor Mode, allowing an included template to be edited and previewed again before export.

## Questions to use when deciding

Choose the workflow by answering these questions:

1. **Does the source footage need more editing?** If yes, export a standalone overlay.
2. **Is transparency required?** If yes, use a supported overlay-only alpha format.
3. **Is the original source file available?** Source Composite cannot proceed without it.
4. **Should Shred Scopes produce the final video and audio together?** If yes, use Source Composite.
5. **Is the source a GoPro `.360` file?** Use its telemetry for an overlay, then complete the video in another compatible application.
6. **Will several graphics be arranged in another editor?** Exporting them separately can provide more control there; arranging them in Source Composite produces one finished file.

## Summary

Use a standalone telemetry overlay when Shred Scopes supplies the animated graphics to a larger post-production workflow. Use Source Composite when Shred Scopes should combine those graphics with the original GoPro footage and audio.

The output, not the telemetry source, is the main distinction. Both methods can use the same compatible data and templates, but they place responsibility for the final composition in different applications.
