#install.packages('dummies')
#install.packages('corrplot')
#install.packages("tidyverse")
#install.packages("funModeling")
#install.packages("Hmisc", dependencies = TRUE)

suppressMessages(library(funModeling))
suppressMessages(library(tidyverse))
suppressMessages(library(Hmisc))
library('funModeling') 
library('tidyverse')
library('Hmisc')
library('dummies')
library('ROCR')
library('corrplot')

setwd('C:/Users/39333/Desktop')
dataframe <- read.csv(file = 'Placement_Data_Full_Class.csv', header = T, na.strings = c(""))
### A Quick look at the database
str(dataframe)
df <- dataframe[ -c(1)]
df[df==""] <- NA
sapply(df,function(x) sum(is.na(x)))
sapply(df, function(x) length(unique(x)))

#Analising Numerical

numerical =df %>% select(ssc_p, hsc_p, degree_p, etest_p, mba_p, salary)

basic_eda <- function(numerical)

 {  plot_num(numerical)
  summary(numerical)
}

basic_eda(numerical)
#count(names(numerical))

categorical =df %>% select(gender, ssc_b, hsc_b, hsc_s, degree_t, workex,specialisation, status)

#to run separately below lines (37 to 44, need to be run separately )

freq(data=categorical, input = c('gender','ssc_b','hsc_b', 'hsc_s', 'degree_t', 'workex'
                                 , 'specialisation', 'status'), plot = FALSE )

df.new = subset(df, select = c(2,4,7,10,12))
print(names(df.new))


df.cor = df.new
options(warn=-1)
df.cor$gender = dummy(df$gender)
df.cor$ssc_b = dummy(df$ssc_b)
df.cor$hsc_b = dummy(df$hsc_b)
df.cor$hsc_s = dummy(df$hsc_s)
df.cor$degree_t = dummy(df$degree_t)
df.cor$workex = dummy(df$workex)
df.cor$specialisation = dummy(df$specialisation)
df.cor$status = dummy(df$status)
options(warn=0)
print(names(df.cor))


df.cor.plot <- cor(df.cor)
corrplot(df.cor.plot,method = c("square") , type = "lower")

df.new$gender = factor(df$gender)
df.new$ssc_b = factor(df$ssc_b)
df.new$hsc_b = factor(df$hsc_b)
df.new$hsc_s = factor(df$hsc_s)
df.new$degree_t = factor(df$degree_t)
df.new$workex = factor(df$workex)
df.new$specialisation = factor(df$specialisation)
df.new$status = factor(df$status)
str(df.new)
print(names(df.new))

model1 <- glm(status ~. ,family=binomial(link='logit'),data=df.new)
summary(model1)

df = df.new[, c("status","ssc_p" ,"hsc_p", "degree_p", "mba_p", "workex")]
print(names(df))
model2 <- glm(status ~. ,family=binomial(link='logit'),data=df)
summary(model2)

exp(model2$coefficients)
confint(model2)

print("comparing the differences between the null model and the model with variables ")

chi.model2 <- model2$null.deviance - model2$deviance
print(paste('difference in variance',chi.model2))
degfree.model2 <- model2$df.null - model2$df.residual
print(paste('difference in variance',degfree.model2))
p.value <- ( 1- pchisq(chi.model2,degfree.model2))
print(paste('p-values is ',p.value))

anova
anova(model2, test="Chisq")

df$status <- ifelse(df$status == 'Placed',1,0)
train <- df[1:170,]
test <- df[170:215,]

modelTrain <- glm(status ~. ,family=binomial(link='logit'),data=train)
fitted.results <- predict(modelTrain,newdata = test, type='response')
fitted.results <- ifelse(fitted.results > 0.5,1,0)
misClasificError <- mean(fitted.results != test$status)
print(paste('Accuracy',1-misClasificError))

p <- predict(modelTrain,newdata = test, type='response')
pr <- prediction(p, test$status)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf,colorize=TRUE)
abline(0,1,lwd = 2, lty = 2)

auc <- performance(pr, measure = "auc")
auc <- auc@y.values[[1]]
auc
