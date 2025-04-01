# Momentum-Equations-in-Astrophysics
With this app, available in MATLAB (through App Designer) and Python (through tkinter), the user can calculate and represent 3D trajectories of bodies in different planets using momentum equations.
Momentum equations are the following:

![problema7](https://github.com/user-attachments/assets/7cef3cdc-db36-42b5-8b65-1e2c2e15a0e3)

Limitations of this app concerns the fact that we don't include pressure gradient (P) and frictional forces (F_r).

# Python app

The interface available in Python is the following:

![imagen](https://github.com/user-attachments/assets/62939f62-7a6e-42b6-aa4f-edafd0489c79)

The user needs to specify:
- Planet's Angular Velocity (rad/s): Omega.
- Latitude of the object in the planet (rad): phi.
- Planet Radius (m): a.
- Simulation time (s): t.
- Initial Conditions (in IS Units): this initial conditions refer to velocity conditions (u0 (zonal), v0 (meridional) and w0 (vertical)) and positional conditions (x0, y0 and z0).

After the parameters are specified, the user can represent the curves pressing the "Calculate" button. The user can save the figure, rename the curves, load data (in .csv), export data, hide or show curves using the menu "File".

The "Reset Figure" button cleans the figure and removes all the curves.

Also, the user can access the functionalities and documentation of the app in the menu "Help".
