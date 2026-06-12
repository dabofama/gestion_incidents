-- ============================================
-- Script SQL - Gestion des Tickets d'Incidents
-- Base de données : MySQL
-- ============================================

CREATE DATABASE IF NOT EXISTS gestion_incidents;
USE gestion_incidents;

-- Table utilisateur
CREATE TABLE IF NOT EXISTS utilisateur (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    role ENUM('UTILISATEUR', 'TECHNICIEN', 'ADMIN') NOT NULL,
    service VARCHAR(100),
    date_creation DATE DEFAULT (CURRENT_DATE)
);

-- Table incident
CREATE TABLE IF NOT EXISTS incident (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    priorite ENUM('BASSE', 'MOYENNE', 'HAUTE', 'CRITIQUE') NOT NULL,
    statut ENUM('OUVERT', 'EN_COURS', 'RESOLU', 'FERME') DEFAULT 'OUVERT',
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
    utilisateur_id INT NOT NULL,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateur(id)
);

-- Table intervention
CREATE TABLE IF NOT EXISTS intervention (
    id INT AUTO_INCREMENT PRIMARY KEY,
    commentaire TEXT NOT NULL,
    duree_minutes INT DEFAULT 0,
    date_intervention DATETIME DEFAULT CURRENT_TIMESTAMP,
    incident_id INT NOT NULL,
    technicien_id INT NOT NULL,
    FOREIGN KEY (incident_id) REFERENCES incident(id),
    FOREIGN KEY (technicien_id) REFERENCES utilisateur(id)
);
