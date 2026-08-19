import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Compute Collatz sequence for n = 27
n = 27
seq = [n]
while n != 1:
    n = (3 * n + 1) if (n % 2 != 0) else (n // 2)
    seq.append(n)

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, len(seq) + 2)
ax.set_ylim(0, max(seq) * 1.1)
ax.set_title(f"Collatz Trajectory: n=27 (Peak: {max(seq):,})", fontsize=14, fontweight="bold")
ax.set_xlabel("Steps")
ax.set_ylabel("Value")
ax.grid(True, linestyle="--", alpha=0.6)

line, = ax.plot([], [], lw=2, color="#1f77b4")
point, = ax.plot([], [], "ro", markersize=6)

def update(frame):
    line.set_data(range(frame + 1), seq[:frame + 1])
    point.set_data([frame], [seq[frame]])
    return line, point

ani = animation.FuncAnimation(fig, update, frames=len(seq), interval=50, repeat=False)
plt.show()
