# Integrated Seismic Resilience of Low-Damage RC Buildings

## Overview

This project investigates the seismic performance of conventional and low-damage reinforced-concrete (RC) buildings, with emphasis on structural response, residual drift, non-structural element (NSE) damage and post-earthquake recovery.

## Objectives

* Compare conventional and low-damage RC structural systems under earthquake loading.
* Evaluate maximum and residual inter-storey drift.
* Investigate the relationship between structural drift and damage to drift-sensitive non-structural elements.
* Develop damage-state and fragility relationships for selected NSEs.
* Assess implications for repairability and post-earthquake functionality.

## Methodology

**RC Building Model → Modal Analysis → Nonlinear Seismic Analysis → Inter-Storey Drift → NSE Damage Assessment → Fragility Analysis → Recovery Assessment**

### Structural Response

The study considers:

* Storey displacement
* Inter-storey drift ratio
* Residual drift
* Base shear
* Floor acceleration
* Plastic hinge development
* Energy dissipation

### Non-Structural Elements

The initial assessment considers:

* Partition walls
* Glazing systems
* Suspended ceilings

### Seismic Performance

Structural and non-structural damage are evaluated across multiple earthquake intensity levels to investigate the relationship between seismic demand and building functionality.

## Tools

* ETABS / OpenSees
* Python
* Excel
* NumPy
* Matplotlib

## Project Status

**Ongoing independent research project**

## Research Focus

Structural Engineering | Earthquake Engineering | Low-Damage Design | Seismic Resilience | Non-Structural Elements | Fragility Assessment
## Preliminary Results

### Inter-Storey Drift Profile
### Illustrative Earthquake Ground Motion

The following ground-motion input is used to demonstrate the seismic-analysis workflow.

![Illustrative Earthquake Ground Motion](illustrative_ground_motion.png)

> Note: This is an illustrative input signal used for workflow development. It is not an actual recorded earthquake ground motion.

The preliminary model demonstrates the calculation and visualization of inter-storey drift across the building height.

![Preliminary Inter-Storey Drift Profile](results/preliminary_drift_profile.png)

> Note: The current figure uses illustrative displacement data for development of the analysis workflow. It will be replaced with results from the validated nonlinear seismic model.
### SDOF Seismic Response

A simplified single-degree-of-freedom (SDOF) model is used to demonstrate the relationship between earthquake ground motion and structural displacement response.

![SDOF Seismic Response](sdof_response.png)

> Note: The current response is generated using an illustrative ground-motion input and a simplified numerical model. Further development will use validated structural models and recorded earthquake data.
### 6-Storey Building Modal Analysis

A simplified six-degree-of-freedom shear-building model was developed to investigate the dynamic characteristics of the representative RC building.

The model uses the assumed building mass and storey stiffness to estimate the natural periods and mode shapes.

#### First Mode Shape

![First Mode Shape](first_mode_shape.png)

The first mode represents the fundamental lateral deformation pattern of the building, with increasing displacement toward the upper storeys.

> Note: The current model uses preliminary assumed mass and stiffness properties. These parameters will be refined during further development and validation.
