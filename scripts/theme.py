"""Color system shared by the README badges and the artwork.

The four stage colors are sampled from the survey's pipeline figure (pastel fill,
saturated border), so the repository looks like the paper it accompanies.
"""

PALETTE = {
    "evidence-acquisition": {"fill": "#fcf0f7", "border": "#cf7fb3", "badge": "c0609f", "ink": "#8a3a6e", "icon": "acquisition"},
    "memory-state": {"fill": "#fdf7dc", "border": "#d2ac2c", "badge": "b8921a", "ink": "#7a5f0c", "icon": "memory"},
    "control-planning": {"fill": "#eaf3ff", "border": "#5f98dc", "badge": "4a82c9", "ink": "#2c5a96", "icon": "control"},
    "verification-aggregation": {"fill": "#ecf7ee", "border": "#5fae75", "badge": "4a9a62", "ink": "#2f6e43", "icon": "verification"},
}
SHORT = {
    "retrieval-based": "Retrieval", "hierarchical": "Hierarchical", "learned-acquisition": "Learned policies", "programmatic": "Programmatic",
    "textual": "Textual", "structured": "Structured", "compact": "Compact", "streaming": "Streaming",
    "autonomous-tool-use": "Tool use", "multi-agent": "Multi-agent", "learned-control": "Learned control", "fixed-workflow": "Fixed workflow",
    "consensus": "Consensus", "reflection": "Reflection", "confidence": "Confidence", "evidence-alignment": "Alignment",
}
