# How to Format GPS Date and Time in a Telemetry Overlay

GoPro GPS telemetry can provide the recorded date and clock time for a telemetry overlay. A GPS-time data-text layer can display a date, a time, milliseconds, or a combined timestamp, and it can present the clock in UTC, the browser's local time zone, or a selected time zone.

GPS time is different from elapsed time. Use GPS time for a recorded clock or timestamp. Use elapsed time or source timecode for a counter that starts from the beginning of the clip or selected range.

## Confirm that GPS time is available

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio." Load the intended GoPro clip or saved telemetry source and review the available streams.

The source must contain usable GPS time. Choosing the GPS-time stream does not create a timestamp when the camera did not record one.

Open a custom template or create a custom copy of a built-in template before saving changes.

## 1. Add a GPS-time data-text layer

In the Template Editor:

1. Open "Layers."
2. Select "Add Layer" or a plus control labeled "Add layer here."
3. Choose "data·text."
4. Name the layer, such as "GPS clock" or "Recorded date."
5. Select the GPS-time stream under "Stream."

If the stream is shown as unavailable, confirm that the correct source is active and that it contains GPS telemetry.

## 2. Choose the date or time conversion

Open "Convert" and choose the output needed for the overlay. Available GPS-time choices can include a date, a time, a date-and-time combination, a time-zone-aware clock, milliseconds, or a Unix-millisecond value.

Choose according to the intended meaning:

- Date only identifies the calendar day.
- Time only creates a recorded clock.
- Date and time create a complete timestamp.
- Milliseconds add sub-second detail when event timing requires it.
- Unix milliseconds present the numeric timestamp and are generally intended for technical synchronization rather than a viewer-facing clock.

Do not use a Unix-millisecond display when a conventional date or time is expected.

## 3. Choose 12-hour or 24-hour time

For a clock display, choose between 12-hour and 24-hour formatting where the selected conversion offers that option.

A 12-hour clock should include the appropriate AM or PM indicator. A 24-hour clock avoids that indicator and is often more compact. Select one convention and use it consistently throughout the video.

Preview times around noon and midnight if the source crosses either boundary.

## 4. Choose the time zone

The same recorded moment can be displayed in different time zones:

- "UTC time" keeps the clock in Coordinated Universal Time.
- "Local time" uses the local time zone available to the current browser and computer.
- "Custom time zone" uses a selected named time zone.

For a custom zone, enter or choose a valid IANA time-zone name, such as `America/Denver` or `Europe/London`, in the "Time zone" control. A city-based name accounts for the rules associated with that zone more reliably than a fixed informal abbreviation.

Changing the display time zone changes the clock shown in the layer. It does not change the recorded UTC moment in the telemetry.

For repeatable results across computers, use UTC or an explicit custom zone. "Local time" can display differently when the same template is opened on a computer configured for another region.

## 5. Decide whether to show milliseconds

Enable milliseconds when a viewer must compare events within the same second. They can be useful for motorsport timing, jump analysis, or synchronization checks.

Milliseconds make the text wider and update rapidly. Omit them for ordinary recorded-date labels and clocks where the extra precision adds clutter.

After enabling milliseconds, increase the available width or use automatic fitting so the final digits do not leave the canvas.

## 6. Add a prefix, suffix, or separate label

Use "Prefix" or "Suffix" when the label should remain attached to the changing timestamp. Examples include `GPS `, `UTC `, or a short time-zone label.

Use a separate static text layer when the label needs a different size, weight, color, or position. Avoid showing an ambiguous abbreviation when viewers need to know which time zone is displayed.

The label should describe the chosen conversion accurately. A local-time clock should not be labeled UTC.

## 7. Style and fit the timestamp

Choose a font whose digits, punctuation, and AM or PM indicators remain distinct at the intended export size. Then configure:

- Font weight and size
- Fill and stroke
- Letter spacing
- Alignment and baseline
- Shadow where additional separation is needed
- Fixed sizing or automatic fitting
- Maximum width and height for fitted text
- X and Y position

Timestamp strings can be considerably wider than simple numbers. Preview the complete date-and-time form before finalizing the layer size.

## 8. Check the full source range

Play or scrub the timeline and inspect:

- The first and last recorded times
- A change of minute or hour
- Midnight or a date change when present
- Noon in 12-hour format
- Millisecond updates when enabled
- Daylight-saving transitions if the recording spans one
- Frames where GPS telemetry becomes unavailable

Place the template over the source footage in Source Composite and confirm that the clock stays legible over both bright and dark scenes.

## 9. Avoid confusing GPS time with other clocks

Use the correct stream for the intended result:

- GPS time represents the recorded real-world timestamp.
- Elapsed time represents progression through the selected telemetry timeline.
- Source timecode represents a position associated with the media timeline.
- Airtime or another duration stream measures a specific telemetry-derived event.

These clocks can show different values even when they appear on the same frame. Label them clearly when more than one is displayed.

## 10. Save and verify

Use "Save" for an existing custom template or "Template" > "Save As New" for a new version. Reopen the template and confirm the GPS-time stream, conversion, 12-hour or 24-hour setting, time zone, label, and text fitting.

Export a short representative range before processing a long video. The test should show that the timestamp advances correctly and remains inside the intended layout.
