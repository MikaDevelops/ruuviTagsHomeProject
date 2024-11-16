datamodel='''
{
    "tables": [
        {
            "name": "measurements",
            "columns": [
                {
                    "name": "id",
                    "type": "INTEGER",
                    "primary_key": true,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
                {
                    "name": "timestamp",
                    "type": "INTEGER",
                    "primary_key": false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
                {
                    "name": "data_format",
                    "type": "INTEGER",
                    "primary_key": false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
                {
                    "name": "humidity",
                    "type": "REAL",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "temperature",
                    "type": "REAL",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "pressure",
                    "type": "REAL",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "acceleration",
                    "type": "REAL",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "acceleration_x",
                    "type": "INTEGER",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "acceleration_y",
                    "type": "INTEGER",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "acceleration_z",
                    "type": "INTEGER",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "tx_power",
                    "type": "INTEGER",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "battery",
                    "type": "INTEGER",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "movement_counter",
                    "type": "INTEGER",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "measurement_sequence_number",
                    "type": "INTEGER",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "mac",
                    "type": "TEXT",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
				{
                    "name": "rssi",
                    "type": "INTEGER",
                    "primary_key":false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                }
            ]
        },
        {
            "name": "macs",
            "columns": [
                {
                    "name": "id",
                    "type": "INTEGER",
                    "primary_key": true,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
                {
                    "name": "mac",
                    "type": "TEXT",
                    "primary_key": false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
                {
                    "name": "nimi",
                    "type": "INTEGER",
                    "primary_key": false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                },
                {
                    "name": "recorded",
                    "type": "INTEGER",
                    "primary_key": false,
                    "foreign_key":
                    {
                        "is_foreign_key":false,
                        "reference": ""
                    }
                }
            ]
        }
    ]
}
'''