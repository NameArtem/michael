# michael
A/B testing and multi-armed bandit made easy

Supports frequentist and Bayesian A/B tests as well as multi-armed bandits. See `getting_started.ipynb`.

## Installation

To install for the first time:

```
git clone https://bitbucket.org/centralonline/michael/
cd michael
pip install . #normal
pip install -e . #dev
```

To upgrade:
```
cd michael
git pull
```

## To-dos
* [x] Test for proportions
* [ ] Test for real values
* [ ] Test for counts

## Dependencies
* plotnine
* numpy
* pandas