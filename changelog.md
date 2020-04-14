# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres (inasmuch as an index-type project can) to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- Working on improving forest indicators to use satellite data on tree cover changes. Anyone who can help with this please get in touch. As of late 2019 this was not possible to do according to the University of Maryland and Global Forest Watch.
- Considering changing wealth inequality to income inequality.
- Find better source of pupil:teacher ratio data or a better indicator as this one is the most labour-intensive to update. No centralised figures appear to be kept for many countries, and even within many federalised countries.

## [2.7.1] - 2020-14-04
No changelog previously kept as this was previously a solo private project with a less-than-fastidious custodian. Version 2 is a significantly changed version of the indexes published in 2015 and later in 2018. 
### Added
- A new hydrocarbon penalty to account for the fact that some nations are wealthy and thus have sovereign wealth funds and other future-focused spending capacities at the expense of future generations

### Changed
- Env1: Reversion from satellite data to FAO data for forest cover changes despite inaccuracy
- Env2: Ecological footprint now adjusted for GDP to give an "environmental efficiency" of a country
- Env3: Energy is now about energy transition and the difference from 1992.
- Econ1: Wealth inequality was changed to spread the countries more
- Soc1: Pupil:teacher ratio was averaged over 5 years instead of 10.
- Soc3: Changed shape of the curve to be linear, and steeper. Removed projected birthrate function.
- Geometric averaging of dimensions remains but indicators are arithmetically averaged within dimensions. This means there is less overall effect of a very poor score on one indicator, but dimensionally poor scores are still weighted heavily

### Removed
- Satellite data for forests, sadly.

## [1.0.0] - 2017-06-20

### Added
- See 2015 thesis and 2018 folder.
