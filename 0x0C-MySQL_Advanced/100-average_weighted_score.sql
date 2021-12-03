-- SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes and
-- store the average weighted score for all students.
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE w_avg FLOAT;
    SET w_avg = (SELECT SUM(score * weight) / SUM(weight) 
                        FROM users AS User
                        JOIN corrections as Cor ON User.id=Cor.user_id 
                        JOIN projects AS Project ON Cor.project_id=Project.id 
                        WHERE User.id=user_id);
    UPDATE users SET average_score = w_avg WHERE id=user_id;
END
//
DELIMITER ;