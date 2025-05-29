from typing import TYPE_CHECKING

from honeybee.model import Model


def test_type_hints():
    """
    This test isn't meant to do anything, merely to check if type hints work.
    """

    if TYPE_CHECKING:
        model = Model.from_hbjson("some_file.json")

        for room in model.rooms:
            for face in room.faces:
                face.type
                for aperture in face.apertures:
                    pass
