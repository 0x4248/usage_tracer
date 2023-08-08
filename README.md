# Usage Tracer

A simple computer statistics tracer.

## Usage

```bash
python3 tracer/main.py
```

The results will be put in `data/latest.json`. Any old data will be moved to `data/[timestamp].json`.

## Example of data

This is an example of the data that will be put in `data/latest.json`.

```json
{
    "start": "2023-07-14 14:30:51",
    "cpu": [
        [
            11.1,
            "2023-07-14 14:30:51"
        ],
        [
            2.9,
            "2023-07-14 14:30:52"
        ],
        [
            5.9,
            "2023-07-14 14:30:53"
        ],
        [
            2.3,
            "2023-07-14 14:30:54"
        ],
        [
            4.7,
            "2023-07-14 14:30:55"
        ],
        [
            5.1,
            "2023-07-14 14:30:56"
        ]
    ]
}
```