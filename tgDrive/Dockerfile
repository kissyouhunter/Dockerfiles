FROM eclipse-temurin:17-jre-jammy

WORKDIR /app

RUN wget -O /app/app.jar https://github.com/SkyDependence/tgDrive/releases/download/v0.0.9/tgDrive-0.0.9.jar

CMD ["java", "-jar", "app.jar"]