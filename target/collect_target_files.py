from obspy import read
import matplotlib.pyplot as plt
import os

# Input MiniSEED files
input_files = [
    "../../RELLOC_SUPPLEMENT/H02/H02_KEV_BHE.mseed",
    "../../RELLOC_SUPPLEMENT/H02/H02_KEV_BHN.mseed",
    "../../RELLOC_SUPPLEMENT/H02/H02_KEV_BHZ.mseed"
]

for infile in input_files:
    # Read MiniSEED file
    st = read(infile)
    tr = st[0]

    # Build SAC filename
    # Example: H02_KEV_BHE.mseed -> H02_KEV_BHE.sac
    base = os.path.basename(infile)
    sac_name = os.path.splitext(base)[0] + ".sac"
    sac_path = "./" + sac_name

    print(f"Writing SAC file: {sac_path}")

    # Write SAC
    tr.write(sac_path, format="SAC")

    # Plot the trace
    plt.figure(figsize=(10, 4))
    plt.plot(tr.times(), tr.data, linewidth=0.8)
    plt.title(f"Trace: {sac_name}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
