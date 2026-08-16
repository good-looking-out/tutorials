# How to Add Airtime and Jump Duration to GoPro Video

Shred Scopes can use detected in-air events from GoPro motion telemetry to show an "In Air" state and accumulated airtime. The two available stream types serve different purposes:

- "In air" identifies frames inside a detected airtime event.
- "Cumulative airtime" totals the duration of detected airtime events through the current frame.

Cumulative airtime is a running session total. It should not be labeled as the duration of the current individual jump.

## Before starting

Use an original GoPro clip containing the required motion telemetry, or saved telemetry extracted from that clip.

Detected airtime is based on the recorded sensor data. It may not correspond perfectly to every visible hop, drop, or loss of contact, so preview each important event before exporting.

## 1. Load a source with airtime data

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Load the original clip or choose saved telemetry from the account. After Studio prepares the source, check for:

- "In air"
- "Cumulative airtime"

If these streams are unavailable, an airtime template cannot detect events merely from visible video frames.

## 2. Choose or create an airtime template

If the "Airtime" built-in template is available in the template chooser, open it as a starting point. It combines a conditional in-air message with a cumulative airtime value.

To build a custom version:

1. Start a new template.
2. Add a data-text layer for the in-air state.
3. Add another data-text layer for cumulative airtime.
4. Add static labels or background shapes as needed.

The two data layers should remain separate because one is binary state and the other is a duration total.

## 3. Configure the in-air indicator

Select the first data-text layer and map "Stream" to "In air."

The stream uses:

- 1 while a frame is inside a detected airtime event
- 0 while it is not

Use a text map or visibility condition so the layer displays "In Air" only when the value is active. Set the minimum threshold above the inactive value, then preview the frames immediately before takeoff, during airtime, and after landing.

If the label flickers at an event boundary, use the available visibility stabilization controls cautiously. Do not extend the hold so far that the message remains visible well after landing.

## 4. Configure cumulative airtime

Select the second data-text layer and map "Stream" to "Cumulative airtime."

The value uses seconds and increases as detected events accumulate. Format it as:

- Raw seconds with selected decimal precision
- MM:SS
- HH:mm:ss
- Seconds with tenths, hundredths, or milliseconds where available

For short action footage, seconds with one to three decimal places can be easier to interpret than a clock-style duration.

Label this value "Airtime" or "Total Airtime." Do not label it "Current Jump" because it retains the airtime accumulated from earlier events.

## 5. Reset total airtime for a selected segment

To make the cumulative value begin at zero at a selected in point:

1. Set the required in point.
2. Set the required out point.
3. Enable "Rebuild data graphics from range."
4. Confirm that cumulative airtime is zero at the first frame of the rebuilt range.

This is useful when the source contains several activities but the exported segment should count only the selected portion.

## 6. Understand the individual-jump limitation

The standard telemetry choices provide an in-air state and cumulative airtime. They do not provide a separate ready-made stream that resets to zero at every takeoff and stops at each landing.

As a result:

- The in-air label can identify when a detected jump is occurring.
- The cumulative value can show total detected airtime.
- Duration formatting can make that total look like elapsed time.
- The cumulative value should not be presented as the duration of one specific jump.

When individual jump durations are required, use the in-air event boundaries as a review aid and calculate or annotate each event separately in the finishing workflow.

## 7. Preview every event

Scrub through each visible takeoff and landing. Confirm that:

- "In Air" appears only during the expected event.
- Cumulative airtime increases during detected airtime.
- The total remains stable while the camera is not in air.
- Formatting and decimal precision remain readable.
- The label and total do not imply unsupported per-jump precision.

Very small hops or unusual camera motion may not be detected as expected. Base the final overlay on observed event behavior in the active source.

## 8. Save and export

Use "Template" > "Save As New" after modifying a built-in design or completing a custom template.

Export the airtime graphic separately for another editor, or choose "Composite Mode" to place it over the original GoPro footage and export a finished Source Composite video.

Keep the Studio tab open and visible during export.

## If airtime does not appear

Check that:

- The active source contains "In air" and "Cumulative airtime."
- The in-air layer's visibility threshold includes the active value.
- The cumulative layer uses duration or numeric formatting appropriate to seconds.
- The final range was rebuilt if the total should begin at the in point.
- The event was actually detected in the telemetry.

The completed template now shows detected in-air state and total accumulated airtime without misrepresenting the total as an individual jump timer.
