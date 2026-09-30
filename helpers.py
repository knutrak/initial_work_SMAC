import matplotlib.pyplot as plt


def plot_sequence(log):
    t = [e["t"] for e in log]

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

    # 1) Units alive over time
    ax = axes[0]
    ax.step(t, [e["allies_alive"] for e in log], where="post", label="Allies")
    ax.step(t, [e["enemies_alive"] for e in log], where="post", label="Enemies")
    ax.set(title="Units alive", xlabel="Step", ylabel="Count")
    ax.legend()

    # 2) Total health over time
    ax = axes[1]
    ax.plot(t, [e["allies_hp"] for e in log], label="Allies")
    ax.plot(t, [e["enemies_hp"] for e in log], label="Enemies")
    ax.set(title="Total health", xlabel="Step", ylabel="HP")
    ax.legend()

    # 3) Movement trajectories of every unit
    ax = axes[2]
    for team, key, color in [("Ally", "allies_pos", "tab:blue"), ("Enemy", "enemies_pos", "tab:orange")]:
        ids = {k for e in log for k in e[key]}
        for k in ids:
            pts = [e[key][k] for e in log if k in e[key]]
            xs, ys = zip(*pts)
            ax.plot(xs, ys, color=color, alpha=0.7)
            ax.scatter(xs[0], ys[0], color=color, marker="o", s=30)   # start
            ax.scatter(xs[-1], ys[-1], color=color, marker="x", s=50) # last position alive
        ax.plot([], [], color=color, label=team)
    ax.set(title="Unit trajectories (o = start, x = end/death)", xlabel="x", ylabel="y")
    ax.set_aspect("equal")
    ax.legend()

    plt.tight_layout()
    plt.savefig("battle.png", dpi=150)
    plt.show()