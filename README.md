# Integrated Seismic Resilience of Low-Damage RC Buildings

## Overview

This project develops a computational framework for investigating the seismic resilience of reinforced-concrete (RC) buildings, with emphasis on structural deformation, drift-sensitive non-structural elements (NSEs), damage exceedance and post-earthquake recovery.

A simplified six-storey RC building model is currently used to demonstrate the analysis workflow. The project is being progressively developed toward a validated seismic-response and fragility-analysis framework.

## Research Objectives

* Evaluate seismic deformation demands in a representative multi-storey RC building.
* Quantify storey displacement and inter-storey drift.
* Investigate the relationship between drift demand and potential damage to drift-sensitive NSEs.
* Develop a probabilistic framework for NSE damage-state exceedance.
* Examine residual drift and post-earthquake recovery.
* Establish a computational basis for comparing conventional and low-damage structural systems.

## Computational Framework

**Building Model → Modal Analysis → Seismic Response → Inter-Storey Drift → NSE Damage Assessment → Fragility Analysis → Recovery Assessment → Conventional/Low-Damage Comparison**

### Structural Response Parameters

The current framework considers:

* Storey displacement
* Inter-storey drift ratio
* Natural periods and mode shapes
* Residual drift
* Seismic response history
* NSE damage demand

Future development will incorporate additional response quantities including base shear, floor acceleration, plastic hinge development and energy dissipation.

## Representative Building Model

A simplified six-storey shear-building representation is used for preliminary numerical analysis.

| Parameter         |                     Value |
| ----------------- | ------------------------: |
| Number of storeys |                         6 |
| Storey height     |                     3.2 m |
| Plan dimensions   |               20 m × 15 m |
| Concrete          |                       M25 |
| Reinforcement     |                     Fe500 |
| Column size       |              500 × 500 mm |
| Beam size         |              300 × 500 mm |
| Structural system | RC moment-resisting frame |

The current model uses assumed mass and stiffness properties for workflow development. These parameters will be refined as the model progresses toward a more physically representative structural analysis.

## Seismic Response Analysis

An illustrative ground-motion input was first developed to establish the computational workflow.

![Illustrative Earthquake Ground Motion](illustrative_ground_motion.png)

> **Note:** The current ground-motion signal is synthetic and is used only for workflow development. It is not a recorded earthquake ground motion.

A simplified multi-degree-of-freedom building model was subsequently used to estimate seismic displacement response.

![Maximum Storey Displacement](maximum_storey_displacement.png)

The resulting displacement profile forms the basis for the subsequent inter-storey drift analysis.

## Modal Analysis

A six-degree-of-freedom shear-building model was developed to investigate the dynamic characteristics of the representative structure.

The model estimates natural periods and mode shapes from the assumed mass and storey stiffness matrices.

![First Mode Shape](first_mode_shape.png)

> **Note:** The current modal model uses preliminary assumed mass and stiffness properties and is intended for computational workflow development.

## Inter-Storey Drift Analysis

Inter-storey drift ratio is calculated as:

**IDRᵢ = (Δᵢ − Δᵢ₋₁) / hᵢ**

where:

* Δᵢ = lateral displacement at storey *i*
* Δᵢ₋₁ = lateral displacement at the storey below
* hᵢ = storey height

The preliminary model produces the following drift profile:

| Storey | Displacement (m) | Drift Ratio |
| ------ | ---------------: | ----------: |
| 1      |          0.02381 |      0.744% |
| 2      |          0.04670 |      0.715% |
| 3      |          0.06750 |      0.650% |
| 4      |          0.08453 |      0.532% |
| 5      |          0.09659 |      0.377% |
| 6      |          0.10283 |      0.195% |

![Inter-Storey Drift Profile](seismic_drift_profile.png)

The maximum preliminary drift ratio is approximately **0.744% at Storey 1**.

> **Note:** These values are outputs of the current simplified numerical model and should not be interpreted as validated structural design results.

## Non-Structural Element Damage Assessment

Because many NSEs are sensitive to inter-storey deformation, drift demand is used as the primary damage-demand parameter in the preliminary assessment.

The current workflow considers representative drift-sensitive NSE categories such as:

* Partition walls
* Glazing systems
* Suspended ceilings

An illustrative drift-based classification was implemented:

| Storey | Drift Ratio | Illustrative Damage State |
| ------ | ----------: | ------------------------- |
| 1      |      0.744% | Moderate Damage           |
| 2      |      0.715% | Moderate Damage           |
| 3      |      0.650% | Moderate Damage           |
| 4      |      0.532% | Moderate Damage           |
| 5      |      0.377% | Slight Damage             |
| 6      |      0.195% | No / Very Low Damage      |

![NSE Damage Assessment](nse_damage_assessment.png)

> **Note:** The damage thresholds used here are illustrative assumptions for demonstrating the assessment workflow. They are not code limits, experimental results or literature-calibrated damage thresholds.

## NSE Fragility Analysis

A preliminary probabilistic fragility framework was developed to relate drift demand to the probability of exceeding selected NSE damage states.

A lognormal formulation is used in the current implementation:

**P(DS ≥ ds | θ) = Φ[ln(θ/θₘ) / β]**

where:

* θ = drift demand
* θₘ = median drift capacity
* β = logarithmic dispersion
* Φ = standard normal cumulative distribution function

Three illustrative damage states are currently considered:

* Slight Damage
* Moderate Damage
* Severe Damage

![NSE Fragility Curves](nse_fragility_curves.png)

The resulting curves demonstrate the increase in damage-state exceedance probability with increasing drift demand.

> **Note:** The median capacities and dispersion parameter are illustrative assumptions and are not experimentally validated or literature-calibrated. Future development will incorporate published NSE damage-state data and calibrated fragility parameters.

## Residual Drift and Post-Earthquake Recovery

Residual drift is investigated as a potential indicator of post-earthquake repairability and functional recovery.

A normalized recovery index is currently defined as:

**Recovery Index = (1 − Residual Drift / Initial Residual Drift) × 100**

The preliminary illustrative recovery model gives:

| Time After Earthquake | Residual Drift | Recovery Index |
| --------------------: | -------------: | -------------: |
|                   0 h |          0.80% |           0.0% |
|                   6 h |          0.72% |          10.0% |
|                  12 h |          0.62% |          22.5% |
|                  24 h |          0.50% |          37.5% |
|                  48 h |          0.35% |          56.2% |
|                  72 h |          0.22% |          72.5% |
|                 120 h |          0.10% |          87.5% |
|                 168 h |          0.04% |          95.0% |

![Post-Earthquake Residual Drift](residual_drift_recovery.png)

> **Note:** The recovery data are illustrative assumptions used to demonstrate the recovery-analysis workflow. They do not represent measured post-earthquake observations.

## Conventional vs Low-Damage RC Response

A preliminary computational comparison was implemented between the conventional RC response and an illustrative low-damage response scenario.

| Storey | Conventional RC (m) | Low-Damage RC (m) | Illustrative Reduction |
| ------ | ------------------: | ----------------: | ---------------------: |
| 1      |             0.02381 |           0.01600 |                  32.8% |
| 2      |             0.04670 |           0.03100 |                  33.6% |
| 3      |             0.06750 |           0.04500 |                  33.3% |
| 4      |             0.08453 |           0.05700 |                  32.6% |
| 5      |             0.09659 |           0.06600 |                  31.7% |
| 6      |             0.10283 |           0.07100 |                  31.0% |

![Conventional vs Low-Damage RC](conventional_vs_low_damage.png)

The illustrative scenario indicates a displacement reduction of approximately 31–34%.

> **Note:** The low-damage response values are assumed for workflow demonstration and are not obtained from a calibrated low-damage structural model. Therefore, the reported reduction should not be interpreted as validated performance improvement.

## Tools

* Python
* NumPy
* SciPy
* Matplotlib
* Excel
* ETABS / OpenSees *(planned for model validation and advanced analysis)*

## Current Project Status

**Ongoing independent computational research project**

### Current Work

* Simplified multi-storey RC dynamic model
* Modal analysis
* Seismic response simulation
* Inter-storey drift calculation
* Drift-based NSE damage assessment
* Preliminary NSE fragility framework
* Residual drift and recovery workflow
* Conventional vs low-damage response comparison

### Planned Development

* Replace synthetic ground motion with recorded earthquake records.
* Improve numerical time-integration methodology.
* Develop a physically representative nonlinear RC structural model.
* Replace illustrative NSE thresholds with literature-based damage-state criteria.
* Calibrate probabilistic fragility parameters using published data.
* Develop a physically consistent low-damage structural model.
* Investigate the relationship between structural damage, NSE damage and recovery.
* Extend the framework toward probabilistic seismic resilience assessment.

## Research Focus

**Structural Engineering | Earthquake Engineering | Low-Damage Design | Seismic Resilience | Non-Structural Elements | Fragility Assessment | Post-Earthquake Recovery**
