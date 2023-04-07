from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class DateAndTimeFormat:
    date_format: str
    time_format: str

    @property
    def datetime_format(self):
        return f"{self.date_format} {self.time_format}"

    def __str__(self):
        return self.datetime_format


# USA (przykład: 25/01/2021 18:37:00)
# EUROPE (przykład: 25.01.2021 18:37:00)
# ISO (przykład: 2021-01-25 18:37:00)
# UK 12h (przykład: 25/01/2021 06:37:00 PM)
class DatetimePreference(Enum):
    USA = DateAndTimeFormat(date_format="%d/%m/%Y", time_format="%H:%M:%S")
    EUROPE = DateAndTimeFormat(date_format="%d.%m.%Y", time_format="%H:%M:%S")
    ISO = DateAndTimeFormat(date_format="%Y-%m-%d", time_format="%H:%M:%S")
    UK_12H = DateAndTimeFormat(date_format="%d/%m/%Y", time_format="%I:%M:%S %p")

    def __str__(self):
        return f"Format {self.name}: {self.value}"

    @classmethod
    def ordered_instances(cls):
        return [instance for instance in cls.__members__.values()]

    @classmethod
    def instance_by_index(cls, index):
        return cls.ordered_instances()[index]
