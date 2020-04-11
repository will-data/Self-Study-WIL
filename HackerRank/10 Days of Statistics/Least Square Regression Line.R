data <- read.table("stdin",header=F, skip=0)
X = data[,1]; Y = data[,2]

lm_model = lm(Y~X)

cat(round(predict(lm_model, newdata = data.frame(X=80))[[1]],digits=3))