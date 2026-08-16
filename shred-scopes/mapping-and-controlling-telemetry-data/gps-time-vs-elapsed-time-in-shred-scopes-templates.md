# GPS Time vs Elapsed Time in Shred Scopes Templates

GPS time is the absolute UTC timestamp recorded with GoPro GPS telemetry. Elapsed time is the duration since the beginning of the active session or rebuilt timeline range. Choose GPS time for a recorded clock or date and elapsed time for a stopwatch-style display.

The two streams represent different concepts and use different formatting controls.

## Compare the time sources

| Property | GPS time | Elapsed time |
| --- | --- | --- |
| Meaning | Recorded absolute timestamp | Progress since the active start |
| Source unit | UTC milliseconds | Seconds |
| Requires GPS timing | Yes | No GPS clock required |
| Time-zone formatting | UTC, local, or custom | Not applicable |
| Resets after rebuilding a selected range | No recorded timestamp reset | Yes, begins at 0 |
| Typical use | Date, clock, synchronization reference | Timer, duration, segment progress |

## 1. Load the intended source

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and load the GoPro telemetry.

Confirm that "GPS time" is available if an absolute recorded clock is required. Elapsed time can be used for timeline-duration displays even when an absolute GPS timestamp is unavailable.

## 2. Add a GPS-time layer

1. Add a "data·text" layer.
2. Select "GPS time" as its stream.
3. Choose a compatible GPS-time display format.
4. Select 12-hour or 24-hour clock behavior where appropriate.
5. Choose UTC, local time, or a custom time zone.
6. Add a prefix or suffix only when it clarifies the display.

GPS-time formats can include:

- Complete date and time
- Time only
- Date only
- Milliseconds
- A time-zone label
- Unix timestamp in milliseconds

Choose automatic text fitting when a complete timestamp could exceed the available width.

## 3. Choose the GPS time zone

Use:

- "UTC time" for the recorded Coordinated Universal Time value
- "Local time" for the desktop browser computer's local time zone
- "Custom time zone" for a selected IANA time zone

Changing the display time zone changes the shown clock value. It does not change the recorded UTC timestamp.

Use a visible time-zone label when the intended audience could otherwise misinterpret the clock.

## 4. Add an elapsed-time layer

1. Add another "data·text" layer.
2. Select "Elapsed time."
3. Choose a duration display format.
4. Configure size, alignment, prefix, or suffix.

Elapsed time uses seconds and can be displayed as:

- Raw seconds
- MM:SS
- HH:mm:ss
- Hundredths
- Milliseconds
- Seconds with one decimal where available

Use a format appropriate to the source duration and required precision.

## 5. Reset elapsed time for an exported segment

To make a selected segment begin at 0:

1. Set the in point.
2. Set the out point.
3. Choose "Rebuild data graphics from range."
4. Confirm that elapsed time is 0 at the new first frame.

The GPS-time layer continues to show the absolute recorded time corresponding to that frame. This makes it possible to display both the source clock and time since the segment began.

## 6. Use the correct label

Label GPS time as a date, clock, recorded time, or UTC/local time according to its format.

Label elapsed time as elapsed time, duration, session time, or segment time.

Do not label elapsed time as time of day, and do not label GPS time as time since start.

## 7. Distinguish source timecode

Source timecode is separate from GPS time and elapsed time. The export option "Preserve source timecode" concerns timecode metadata used by compatible finishing workflows; it does not turn a template layer into a visible GPS clock or stopwatch.

Add a data-text layer when a visible time display is required.

## 8. Preview formatting and boundaries

Check:

- The first frame
- A minute or hour rollover
- The longest complete date and time
- A daylight or time-zone interpretation relevant to the selected zone
- The first frame after rebuilding a segment
- The final elapsed duration

Confirm that 12-hour displays have clear AM/PM context when needed and that text remains inside the canvas.

## 9. Handle missing GPS time

If "GPS time" is unavailable:

- Confirm that the original source or correct saved telemetry is loaded.
- Check whether the recording contains usable GPS timing.
- Use elapsed time when only a duration display is required.

Do not reconstruct an absolute recording time by labeling elapsed seconds as a clock.

## 10. Save the time display

Save the custom template after confirming the stream, time zone, duration format, range behavior, and labels.

The template now distinguishes an absolute GoPro-recorded timestamp from time elapsed through the active session or selected segment.
