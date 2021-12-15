#!/usr/bin/env Rscript


setwd("/Users/tee/Desktop")

data = read.table("data_out.txt")

values = c()

for(i in 1:dim(data)[1]){
  values = c(values,data[i,1])
}


pdf("coverage.pdf")

barplot(values, ylim = c(0,200), main ="MN136523",xlab="Length: 152476 bp")

dev.off()
