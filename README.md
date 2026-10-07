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
### Non-Structural Element Damage Assessment

A preliminary drift-based assessment was performed to investigate the potential damage state of drift-sensitive non-structural elements (NSEs).

The inter-storey drift ratios obtained from the simplified six-storey seismic response model were used as the damage-demand parameter.

| Storey | Drift Ratio | Illustrative Damage State |
| ------ | ----------: | ------------------------- |
| 1      |      0.744% | Moderate Damage           |
| 2      |      0.715% | Moderate Damage           |
| 3      |      0.650% | Moderate Damage           |
| 4      |      0.532% | Moderate Damage           |
| 5      |      0.377% | Slight Damage             |
| 6      |      0.195% | No / Very Low Damage      |

![NSE Damage Assessment](nse_damage_assessment.png)

> **Note:** The damage thresholds used in the current implementation are illustrative and are intended to demonstrate the damage-assessment workflow. They are not presented as code limits or experimentally validated thresholds. Future work will replace these assumptions with literature-based NSE damage-state criteria and probabilistic fragility relationships.
### NSE Fragility Analysis

A preliminary probabilistic fragility framework was developed to relate inter-storey drift demand to the probability of exceeding selected non-structural element (NSE) damage states.

A lognormal fragility formulation was used to demonstrate the relationship between drift demand and damage-state exceedance probability.

The current illustrative model considers three damage states:

* Slight Damage
* Moderate Damage
* Severe Damage

![NSE Fragility Curves](nse_fragility_curves.png)

The fragility curves demonstrate how the probability of exceeding a given NSE damage state increases with increasing inter-storey drift demand.

> **Note:** The median drift capacities and dispersion parameter used in the current analysis are illustrative assumptions for workflow development. They are not experimentally validated or literature-calibrated values. Future work will incorporate published NSE damage-state data and calibrated fragility parameters.
