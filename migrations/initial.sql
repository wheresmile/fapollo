
-- CREATE DATABASE `fapollo` DEFAULT CHARACTER SET = `utf8mb4`;

-- 创建主页的清单场景
INSERT INTO `checklist_scenes`(`id`, `created_at`, `updated_at`, `deleted_at`, `user_id`, `description`)
VALUES (1, CURRENT_TIME(), CURRENT_TIME(), NULL, 1, '主页');

-- 创建 tab 项
INSERT INTO `fapollo`.`tabs`(`created_at`, `updated_at`, `deleted_at`, `display_name`, `slug`, `location`, `priority`)
VALUES ('2020-07-18 12:54:28', '2020-07-18 12:54:28', NULL, '首页', '', 'home', 0);
INSERT INTO `fapollo`.`tabs`(`created_at`, `updated_at`, `deleted_at`, `display_name`, `slug`, `location`, `priority`)
VALUES ('2020-07-18 12:54:28', '2020-07-18 12:54:28', NULL, '今日清单', 'checklist', 'home', 1);
INSERT INTO `fapollo`.`tabs`(`created_at`, `updated_at`, `deleted_at`, `display_name`, `slug`, `location`, `priority`)
VALUES ('2020-07-18 12:54:28', '2020-07-18 12:54:28', NULL, '没了', 'motto', 'home', 2);