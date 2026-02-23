from obspy import read, UTCDateTime
import matplotlib.pyplot as plt
import os

# Input MiniSEED files
input_files = [
    "../../RELLOC_SUPPLEMENT/H01/H01_KEV_BHE.mseed",
    "../../RELLOC_SUPPLEMENT/H01/H01_KEV_BHN.mseed",
    "../../RELLOC_SUPPLEMENT/H01/H01_KEV_BHZ.mseed",
]

# Relative window in seconds from the trace start
t0_rel = 60.0
t1_rel = 120.0

for infile in input_files:
    # Read MiniSEED file
    st = read(infile)
    tr = st[0]

    # Build time window relative to the trace start
    t0 = tr.stats.starttime + t0_rel
    t1 = tr.stats.starttime + t1_rel

    # Make a copy so we don't modify the original trace
    tr_seg = tr.copy()

    # Trim/slice to the desired window (nearest sample ensures we get data if exact times fall between samples)
    tr_seg.trim(starttime=t0, endtime=t1, nearest_sample=True, pad=False)

    # Build SAC filename
    base = os.path.basename(infile)               # e.g., H01_KEV_BHE.mseed
    sac_name = os.path.splitext(base)[0] + ".sac" # -> H01_KEV_BHE.sac
    sac_path = "./" + sac_name

    # Informative log
    print(f"Writing SAC (60–120 s segment): {sac_path}")
    print(f"  Segment start (UTC): {tr_seg.stats.starttime}")
    print(f"  Segment end   (UTC): {tr_seg.stats.endtime}")
    print(f"  Samples: {tr_seg.stats.npts}, Sampling rate: {tr_seg.stats.sampling_rate} Hz")

    # Write SAC
    tr_seg.write(sac_path, format="SAC")

    # Plot the clipped segment against relative time (seconds from segment start)
    times_rel = tr_seg.times()  # starts at 0 for the trimmed trace
    plt.figure(figsize=(10, 4))
    plt.plot(times_rel, tr_seg.data, linewidth=0.8)
    plt.title(f"Trace segment 60–120 s: {sac_name}")
    plt.xlabel("Time since segment start (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
