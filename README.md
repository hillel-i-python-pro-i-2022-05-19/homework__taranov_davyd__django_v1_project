# Django application

---

## ð  Homework

Homework related actions.

### â¶ï¸ Run

Make all actions needed for run homework from zero.

```shell
make d-homework-i-run
```

#### After, go to [http://localhost:8000](http://localhost:8000)

### ð® Purge

Make all actions needed for run homework from zero.

```shell
make d-homework-i-purge
```

---

## ðï¸ Preparation

Make some initialization steps. For example, copy configs.

```shell
make init-configs-i-dev
```

---

## ð³ Docker

Use services in dockers.

### â¶ï¸ Run

Just run

```shell
make d-run
```

### â¯ï¸ Run extended

Shutdown previous, run in detached mode, follow logs

```shell
make d-run-i-extended
```

### â¹ï¸Stop

Stop services

```shell
make d-stop
```

### ð® Purge

Purge all data related with services

```shell
make d-purge
```

## ð  Creat date

Just run

```shell
make create-data
```