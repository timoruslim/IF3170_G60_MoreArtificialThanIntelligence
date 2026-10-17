import random
import plotly.graph_objects as go
import plotly.express as px
from .engine import *

def draw_package(package, x0, y0, z0, dx, dy, dz, origin=(0,0,0), color='red', opacity=1, name='Box'):

   ox, oy, oz = origin
   x0, y0, z0 = x0 + ox, y0 + oy, z0 + oz

   x = [x0, x0 + dx, x0 + dx, x0, x0, x0 + dx, x0 + dx, x0]
   y = [y0, y0, y0 + dy, y0 + dy, y0, y0, y0 + dy, y0 + dy]
   z = [z0, z0, z0, z0, z0 + dz, z0 + dz, z0 + dz, z0 + dz]

   info = (
      f"<b>ID:</b> {package.id}<br>"
      f"<b>Position in truck (x, y, z):</b> {x0 - ox}, {y0 - oy}, {z0 - oz}<br>"
      f"<b>Size:</b> {dx}x{dy}x{dz}<br>"
      f"<b>Value:</b> {package.value}<br>"
      f"<b>Weight:</b> {package.weight}<br>"
      f"<b>Is_Fragile:</b> {package.is_fragile}<br>"
      f"<b>ETA:</b> {package.eta}"
   )
   hover_texts = [info] * len(x)

   return go.Mesh3d(
      x=x, y=y, z=z,
      alphahull=0, 
      color=color,
      opacity=opacity,
      flatshading=True,
      name=name,
      hovertext=hover_texts,
      hovertemplate="%{hovertext}<extra></extra>",
      showlegend=False
   )

def draw_truck(truck, origin=(0,0,0), color='black', name='Truck'):

   ox, oy, oz = origin
   width, length, height = truck.width, truck.length, truck.height

   x = [
      ox, ox + width, ox + width, ox, ox, None,
      ox, ox + width, ox + width, ox, ox, None,
      ox, ox, None,
      ox + width, ox + width, None,
      ox + width, ox + width, None,
      ox, ox, None
   ]

   y = [
      oy, oy, oy + length, oy + length, oy, None,
      oy, oy, oy + length, oy + length, oy, None,
      oy, oy, None,
      oy, oy, None,
      oy + length, oy + length, None,
      oy + length, oy + length, None
   ]

   z = [
      oz, oz, oz, oz, oz, None,
      oz + height, oz + height, oz + height, oz + height, oz + height, None,
      oz, oz + height, None,
      oz, oz + height, None,
      oz, oz + height, None,
      oz, oz + height, None
   ]

   info = (
      f"<b>ID:</b> {truck.id}<br>"
      f"<b>Size:</b> {width}x{length}x{height}<br>"
      f"<b>Max_Capacity:</b> {truck.max_capacity}<br>"
   )
   hover_texts = [info] * len(x)

   return go.Scatter3d(
      x=x, y=y, z=z,
      mode='lines',
      line=dict(color=color, width=3),
      name=name,
      hovertext=hover_texts,
      hovertemplate="%{hovertext}<extra></extra>",
      showlegend=False
   )

def draw_unassigned_area(width, length, origin=(0,0,0), name="Unassigned Area"):
   ox, oy, oz = origin

   x = [ox, ox + width, ox + width, ox, ox]
   y = [oy, oy, oy + length, oy + length, oy]
   z = [oz, oz, oz, oz, oz]

   return go.Scatter3d(
      x=x, y=y, z=z,
      mode='lines',
      line=dict(color='black', width=3, dash='dashdot'),
      name=name,
      showlegend=False
   )

def draw_state(state, truck_gap=None):

   x_offset = 0
   if truck_gap is None:
      truck_gap = max(truck.width for truck in state.trucks) * 0.2

   drawings = []
   PALETTE = px.colors.qualitative.Plotly

   # Packages in trucks
   for truck in state.trucks:

      origin = (x_offset, 0, 0)
      
      truck_drawing = draw_truck(truck, origin=origin, name=f'Truck {truck.id}')
      drawings.append(truck_drawing)

      packages_in_truck = state.get_packages_in_truck(truck.id)
      for package, placement in packages_in_truck:

         x, y, z = placement.x, placement.y, placement.z
         dx, dy, dz = package.get_dimensions(placement.orientation)

         package_drawing = draw_package(package, x, y, z, dx, dy, dz, origin=origin, color=random.choice(PALETTE), name=f'Package {package.id}')
         drawings.append(package_drawing)

      x_offset += truck.width + truck_gap

   # Packages outside trucks
   unassigned_packages = state.get_packages_outside()

   if unassigned_packages:

      x_max = 0
      y_offset = 1
      origin = (x_offset, y_offset, 0)

      for package in unassigned_packages:

         dx, dy, dz = package.get_dimensions(0)
         x, y, z = 1, y_offset, 0
         if dx >= x_max:
            x_max = dx

         package_drawing = draw_package(package, x, y, z, dx, dy, dz, origin=origin, color=random.choice(PALETTE), name=f'Package {package.id}')
         drawings.append(package_drawing)

         y_offset += dy + 1

      unassigned_area_drawing = draw_unassigned_area(x_max + 2, y_offset, origin=origin, name="Unassigned Area")
      drawings.append(unassigned_area_drawing)

   fig = go.Figure(data=drawings)

   fig.update_scenes(
      xaxis=dict(
         showticklabels=False, 
         ticks="", 
         title="", 
         showbackground=False, 
         showgrid=False, 
         zeroline=False
      ),
      yaxis=dict(
         showticklabels=False,
         ticks="",
         title="",
         showbackground=False, 
         showgrid=False,
         zeroline=False
      ),
      zaxis=dict(
         showticklabels=False,
         ticks="",
         title="",
         showbackground=False, 
         showgrid=False,
         zeroline=False
      ),
      aspectmode="data"
   )

   fig.update_layout(
      margin=dict(l=0, r=0, t=0, b=0, pad=0)
   )

   fig.show()