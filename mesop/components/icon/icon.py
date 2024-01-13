import mesop.components.icon.icon_pb2 as icon_pb
from mesop.component_helpers import (
  Style,
  insert_component,
  register_native_component,
  to_style_proto,
)


@register_native_component
def icon(
  icon: str | None = None,
  *,
  key: str | None = None,
  style: Style | None = None,
):
  """Creates a Icon component.

  Args:
    key: Unique identifier for this component instance.
    icon: Name of the [Material Symbols icon](https://fonts.google.com/icons).
    style: Inline styles
  """
  insert_component(
    key=key,
    type_name="icon",
    proto=icon_pb.IconType(
      icon=icon,
    ),
    style=to_style_proto(style) if style else None,
  )
