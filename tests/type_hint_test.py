from typing import TYPE_CHECKING

from honeybee.model import Model
from honeybee.boundarycondition import Surface


def test_type_hints():
    """
    This test isn't meant to do anything, merely to check if type hints work.
    """

    if TYPE_CHECKING:
        model = Model.from_hbjson("some_file.json")

        for room in model.rooms:
            room.volume
            for face in room.faces:
                roomA_id = face.identifier
                face.type
                if type(face.boundary_condition) is Surface:
                    roomB_id = face.boundary_condition.boundary_condition_objects[0]

                opening_area = sum(aperture.area for aperture in face.apertures)
