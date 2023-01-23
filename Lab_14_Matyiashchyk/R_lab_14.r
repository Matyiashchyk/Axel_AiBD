   
install.packages("ggplot2")
install.packages("GGally")
library(cluster)
library(magrittr)


##### Zadanie 1

lista <- 1:10 # 1 
lista %<>%log2()%>% sin() %>% sum() %>% sqrt() # 2
print(lista)
data(iris) # 3 
print(head(iris)) #4
avg <- iris %>% # 5
    aggregate(.~Species, .,mean)
print(avg)

##### Zadanie 2
library("ggplot2") # dla tworzenia wykresów(wizualizacji)
library("GGally")
a <- ggplot(iris, aes(x = Sepal.Width)) +
    geom_histogram(aes(fill = Species, color = Species), bins = 20) +
    geom_vline(data = avg, aes(xintercept = Sepal.Width, color = Species), linetype = "dashed")+
    labs(x = 'x_axis', y = 'y_axis', title = 'title')
ggsave("D:/Education/3_rok_AGH/5_Semestr/AiBD/Wykresy/graphic.jpg", plot = a)

a<- ggpairs(data = iris, aes(color = Species))
ggsave("D:/Education/3_rok_AGH/5_Semestr/AiBD/Wykresy/graphic2.jpg", plot = a)

##### Zadanie 3
x <- iris[,1:4]
y <- iris[,5]
dane <- c()

for (i in 1:10){
    kmeans_result <- kmeans(x,i)
    dane <- append(dane, kmeans_result$tot.withinss)
}

a <- ggplot(data.frame(iteration = 1:length(dane), value = dane), aes(x = iteration, y = dane))+geom_line()
ggsave("D:/Education/3_rok_AGH/5_Semestr/AiBD/Wykresy/graphic3.jpg", plot = a)

kmeans_result <- kmeans(x,3)
a <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color = kmeans_result$cluster))+geom_point()
ggsave("D:/Education/3_rok_AGH/5_Semestr/AiBD/Wykresy/graphic4.jpg", plot = a)

a<-ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color = Species))+ geom_point()
ggsave("D:/Education/3_rok_AGH/5_Semestr/AiBD/Wykresy/graphic5.jpg", plot = a)