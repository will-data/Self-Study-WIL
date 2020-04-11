library(dplyr)

f <- file("stdin")
on.exit(close(f))

# Get data from input (the hardest part!)
## I got solution below from the discussion, thanks.
T <- readLines(f) %>%
  strsplit(" ") %>%
  lapply(as.numeric)
m <- T[[1]][1]; n <- T[[1]][2]
train <- T[2:(2+n-1)]
train <- data.frame(t(data.frame(train)))
q <- T[[2+n]][1]
test <- T[(2+n+1):(2+n+q)]
test <- data.frame(t(data.frame(test)))

# Do the modelling 
formula <- as.formula(paste(tail(names(train), 1), "~ ."))
model <- lm(formula, train)
predict(model,test) %>%
  round(2) %>%
  format(nsmall = 2) %>%
  write(stdout())