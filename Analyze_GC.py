from Bio import SeqIO
import matplotlib.pyplot as plt

record = SeqIO.read("Enterobacteria phage lambda_complete genome.fasta", "fasta")
sequence = record.seq
print(f"Analyzing: {record.description}")
print(f"Length: {len(sequence)} bp")

window_size = 500
step_size = 100
positions = []
gc_values = []

for i in range(0, len(sequence) - window_size, step_size):
    subseq = sequence[i:i + window_size]
    g_count = subseq.count("G")
    c_count = subseq.count("C")
    gc_percent = (g_count + c_count)/len(subseq) * 100

    positions.append(i)
    gc_values.append(gc_percent)

plt.figure(figsize=(12,6))
plt.plot(positions, gc_values, color='blue', linewidth=1)
plt.title(f"GC content distribution of {record.id}")
plt.xlabel("Genome position (bp)")
plt.ylabel("GC content (%)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
