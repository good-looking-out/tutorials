# How to Create an Animated GPS Route Overlay from GoPro Footage

An animated GPS route overlay draws the path recorded by a GoPro and shows progress along that path as the video plays. Shred Scopes can render the route as a standalone telemetry graphic or position it over the source footage in Source Composite.

The source must contain usable latitude and longitude samples.

## Before starting

Use an original GoPro recording made with GPS enabled and a usable satellite lock, or load telemetry previously extracted from that recording.

Route quality depends on the recorded positions. A template can smooth the drawn path, but it cannot restore GPS points that the camera did not record.

## 1. Load a source with GPS data

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Choose "Choose Clip" for a local original or "Choose Metadata from Account" for a saved extraction. Wait for Studio to prepare the source, then confirm that "GPS path" is available.

If only speed or motion data appears, the source may not contain usable position coordinates.

## 2. Choose a GPS path template

Select a route design at the "Choose Template" step. GPS path templates are available in collections such as:

- Black Diamond GPS Path
- Flagship GPS Path
- Swell GPS Path
- Trailhead GPS Path

These templates are unit agnostic because a path is drawn from coordinate pairs rather than displayed in miles or kilometers.

The selected design opens in the Template Editor.

## 3. Understand the route elements

A GPS path graphic can contain three visually distinct parts:

- The track, representing the route shape
- The progress line, representing the part reached at the current frame
- The position dot, marking the current location on the route

Play the preview and confirm that progress and the dot advance as the timeline moves.

If a custom route graphic is being created, add or select a data-graphic layer, choose the GPS path graphic, and map its input to "GPS path."

## 4. Adjust the route geometry

Select the GPS path layer and use its layout controls to change:

- X and Y position
- Width and height
- Rotation
- Route smoothing

Preserve enough width and height for the recorded route's shape. Excessively narrow dimensions can make a wide route difficult to recognize, while excessive smoothing can remove meaningful corners or switchbacks.

Use smoothing only to reduce distracting sharp changes in the drawn line. Preview recognizable route sections after every substantial change.

## 5. Style the route

The GPS path controls allow separate styling for the track, progress, and position dot.

Configure:

- Track and progress colors
- Track and progress stroke widths
- Solid, dashed, or dotted line styles
- Dash length, gap, and offset where applicable
- Dot fill, stroke, outline width, and radius

Use enough contrast to distinguish completed progress from the remaining route. If the graphic will be placed over changing video, add a contrasting outline or surrounding shape rather than relying on one thin line.

## 6. Set the timeline range

The route is tied to the active telemetry timeline. If only part of the source should be exported:

1. Set the required in point.
2. Set the required out point.
3. Enable "Rebuild data graphics from range" when the route should exclude telemetry before the in point and after the out point.
4. Review the rebuilt path from the new beginning to the new end.

Without rebuilding, a shortened export can still reflect route data outside the intended segment. Rebuilding makes range-dependent graphics use the selected portion and resets applicable cumulative values at the new start.

Choose the final range before making detailed route-sizing decisions because a rebuilt segment can have a different shape and aspect ratio from the complete recording.

## 7. Preview route progress

Inspect the route at:

- The first frame of the active range
- Several intermediate positions
- Turns, loops, and route crossings
- The final frame

Confirm that the position dot stays on the path and that progress moves in the expected direction. A poor satellite lock can create jumps or straight lines between widely separated samples; smoothing may reduce visual sharpness but cannot make missing positions accurate.

## 8. Save and export

If a built-in template was customized, use "Template" > "Save As New" to retain a custom copy.

For a standalone route overlay, choose a transparency-capable format in the Template Editor when the result will be placed over video elsewhere. Select "Export" and keep the Studio tab open and visible until rendering completes.

For a finished GoPro telemetry video, choose "Composite Mode," place the route over the source video, check its scale against several frames, and export the Source Composite result.

## If the route is missing or unsuitable

Check that:

- The selected file is the original GoPro recording.
- GPS path data is listed for the active source.
- GPS was enabled and had a usable lock during recording.
- The path layer is mapped to "GPS path."
- The graphic has nonzero width and height and remains visible on the canvas.
- The active range contains the intended route segment.
- Track, progress, and dot colors contrast with the background.

The completed overlay now shows the recorded route and the camera's progress through it over the selected timeline range.
