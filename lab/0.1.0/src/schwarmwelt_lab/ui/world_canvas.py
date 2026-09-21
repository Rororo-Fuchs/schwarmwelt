from __future__ import annotations

import colorsys
import math
import tkinter as tk
from typing import Callable, Any


class WorldCanvas(tk.Canvas):
    def __init__(self, master: tk.Misc, on_select: Callable[[int], None], **kwargs: Any) -> None:
        super().__init__(master, background="#111214", highlightthickness=0, **kwargs)
        self.on_select = on_select
        self.snapshot: dict[str, Any] | None = None
        self.selected_agent: int | None = None
        self.agent_points: dict[int, tuple[float, float, float]] = {}
        self.bind("<Button-1>", self._click)
        self.bind("<Configure>", lambda _event: self.redraw())

    def set_selected(self, agent_id: int | None) -> None:
        self.selected_agent = agent_id
        self.redraw()

    def update_snapshot(self, snapshot: dict[str, Any]) -> None:
        self.snapshot = snapshot
        self.redraw()

    def _layout(self, zones: int) -> tuple[int, int]:
        columns = math.ceil(math.sqrt(zones))
        rows = math.ceil(zones / columns)
        return rows, columns

    def _zone_rect(self, zone: int, zones: int) -> tuple[float, float, float, float]:
        width = max(self.winfo_width(), 100)
        height = max(self.winfo_height(), 100)
        rows, columns = self._layout(zones)
        gap = 12
        margin = 24
        zone_width = (width - 2 * margin - gap * (columns - 1)) / columns
        zone_height = (height - 2 * margin - gap * (rows - 1)) / rows
        row = zone // columns
        column = zone % columns
        x0 = margin + column * (zone_width + gap)
        y0 = margin + row * (zone_height + gap)
        return x0, y0, x0 + zone_width, y0 + zone_height

    def _agent_position(self, agent: dict[str, Any], zones: int) -> tuple[float, float]:
        x0, y0, x1, y1 = self._zone_rect(agent["zone"], zones)
        padding = 16
        x = x0 + padding + agent["x"] * max(1.0, x1 - x0 - 2 * padding)
        y = y0 + padding + agent["y"] * max(1.0, y1 - y0 - 2 * padding)
        return x, y

    def _diagnostic_color(self, agent: dict[str, Any]) -> str:
        value = (float(agent.get("valence_a", 0.0)) + 1.0) / 2.0
        intensity = 0.35 + 0.55 * float(agent.get("valence_b", 0.5))
        hue = 0.64 - 0.56 * value
        red, green, blue = colorsys.hsv_to_rgb(hue, 0.55, intensity)
        return f"#{int(red * 255):02x}{int(green * 255):02x}{int(blue * 255):02x}"

    def redraw(self) -> None:
        self.delete("all")
        self.agent_points.clear()
        if not self.snapshot:
            self.create_text(30, 30, anchor="nw", fill="#d9d9d9", text="Keine Simulation geladen")
            return

        agents = self.snapshot.get("agents", [])
        zones = max((agent.get("zone", 0) for agent in agents), default=0) + 1
        for zone in range(zones):
            x0, y0, x1, y1 = self._zone_rect(zone, zones)
            self.create_rectangle(x0, y0, x1, y1, outline="#4c5056", width=2)
            self.create_text(x0 + 10, y0 + 8, anchor="nw", fill="#737a82", text=f"ZONE {zone + 1}")

        positions = {agent["id"]: self._agent_position(agent, zones) for agent in agents}
        current_tick = self.snapshot.get("tick", 0)
        for pulse in self.snapshot.get("recent_pulses", []):
            if pulse.get("tick", -1) < current_tick - 1:
                continue
            left = positions.get(pulse["left"])
            right = positions.get(pulse["right"])
            if not left or not right:
                continue
            self.create_line(*left, *right, fill="#676d75", width=1, dash=(3, 4))
            mx = (left[0] + right[0]) / 2
            my = (left[1] + right[1]) / 2
            symbols = self.snapshot.get("symbols", [])
            left_symbol = symbols[pulse["left_symbol"]] if pulse["left_symbol"] < len(symbols) else str(pulse["left_symbol"])
            right_symbol = symbols[pulse["right_symbol"]] if pulse["right_symbol"] < len(symbols) else str(pulse["right_symbol"])
            self.create_text(mx, my - 7, fill="#f2f2f2", text=f"{left_symbol} · {right_symbol}", font=("TkDefaultFont", 11, "bold"))
            if self.snapshot.get("diagnostic"):
                self.create_text(
                    mx,
                    my + 9,
                    fill="#9aa1aa",
                    text=f"ĥ {pulse.get('left_estimate')} / {pulse.get('right_estimate')}",
                    font=("TkDefaultFont", 8),
                )

        for agent in agents:
            x, y = positions[agent["id"]]
            radius = 7.5
            fill = self._diagnostic_color(agent) if self.snapshot.get("diagnostic") else "#d7d9dc"
            outline = "#ffffff" if agent["id"] == self.selected_agent else ("#d9a441" if agent.get("newcomer") else "#26282c")
            width = 3 if agent["id"] == self.selected_agent else 1.5
            self.create_oval(x - radius, y - radius, x + radius, y + radius, fill=fill, outline=outline, width=width)
            if agent.get("last_symbol", -1) >= 0:
                symbols = self.snapshot.get("symbols", [])
                symbol = symbols[agent["last_symbol"]] if agent["last_symbol"] < len(symbols) else str(agent["last_symbol"])
                self.create_text(x, y - 15, fill="#eceef0", text=symbol, font=("TkDefaultFont", 9, "bold"))
            self.agent_points[agent["id"]] = (x, y, radius + 5)

        self.create_text(
            18,
            max(self.winfo_height() - 16, 20),
            anchor="sw",
            fill="#777e87",
            text=f"Tick {current_tick} · {self.snapshot.get('title', '')}",
        )

    def _click(self, event: tk.Event) -> None:
        if not self.agent_points:
            return
        nearest: tuple[float, int] | None = None
        for agent_id, (x, y, radius) in self.agent_points.items():
            distance = math.hypot(event.x - x, event.y - y)
            if distance <= radius and (nearest is None or distance < nearest[0]):
                nearest = (distance, agent_id)
        if nearest is not None:
            self.selected_agent = nearest[1]
            self.on_select(nearest[1])
            self.redraw()
