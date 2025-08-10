import csv
from pathlib import Path
from datetime import date


def load_solver_rows(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:

            required_rows = ["bucket_depth_n","trial","time_sec","states_expanded","solution_length","solver","board_size"]
            if any(not row[i] for i in required_rows):     #skip rows missing time_sec (assuming that means the whole row is empty)
                continue

            depth = int(row["bucket_depth_n"])
            trial = int(row["trial"])
            time_sec = float(row["time_sec"])
            states = int(row["states_expanded"])
            solu = int(row["solution_length"])
            board_size = int(row["board_size"])
            solver = row["solver"]
            seed = int(row["seed"]) if row["seed"] else None
            timestamp = row["timestamp"]

            rows.append({
                "bucket_depth_n": depth,
                "trial": trial,
                "time_sec": time_sec,
                "states_expanded": states,
                "solution_length": solu,
                "board_size": board_size,
                "solver": solver,
                "seed": seed,
                "timestamp": timestamp,
            })
    return rows

def aggregate_by_depth(rows):
    agg = {}
    for row in rows:
        depth = row["bucket_depth_n"]
        if depth not in agg:
            agg[depth] = {
                "trials": 0,
                "sum_time_sec": 0.0,
                "sum_states": 0,
                "sum_solu": 0
            }

        agg[depth]["trials"] += 1
        agg[depth]["sum_time_sec"] += row["time_sec"]
        agg[depth]["sum_states"] += row["states_expanded"]
        agg[depth]["sum_solu"] += row["solution_length"]

    for depth, a in agg.items():
        trials = a["trials"] or 1  #guard divide by zero
        a["avg_time_ms"] = (a["sum_time_sec"] / trials) * 1000.0
        a["avg_states"] = a["sum_states"] / trials
        a["avg_solu"] = a["sum_solu"] / trials

    for i in ["sum_time_sec", "sum_states", "sum_solu"]:
        del a[i]    #delete intermediate sums

    return agg


def render_markdown(agg, board_size, title_solver):
    today = date.today().isoformat()
    title = f"# {title_solver} -Benchmark Summary- [{board_size}x{board_size}]"
    datelog = f"Generated: {today}"

    header = "| Depth (N) | Trials | Avg Time (ms) | Avg States | Avg Soln Len |"
    sep    = "|-----------|--------|---------------|------------|--------------|"

    depths = sorted(agg.keys())

    data_rows = []
    for d in depths:
        a = agg[d]

        trials = a["trials"]
        avg_ms = a["avg_time_ms"]
        avg_states = a["avg_states"]
        avg_solu = a["avg_solu"]
        
        row = (
            f"| {d:<9} | {trials:<6} | {avg_ms:<13.3f} | "
            f"{avg_states:<10.0f} | {avg_solu:<12.1f} |"
        )


        data_rows.append(row)

    lines = [title, datelog, "", header, sep] + data_rows
    markdown = "\n".join(lines) + "\n"

    out_path = Path("docs") / f"bfs_summary_{today}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")



#agg = aggregate_by_depth(load_solver_rows(Path("data/bfs_runs.csv")))
#print(agg[10])

render_markdown(aggregate_by_depth(load_solver_rows(Path("data/bfs_runs.csv"))), 3, "BFS")