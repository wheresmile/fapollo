
-- CREATE DATABASE `fapollo` DEFAULT CHARACTER SET = `utf8mb4`;

-- 创建主页的清单场景
INSERT INTO `checklist_scenes`(`id`, `created_at`, `updated_at`, `deleted_at`, `user_id`, `description`)
VALUES (1, CURRENT_TIME(), CURRENT_TIME(), NULL, 1, '主页');

-- 创建 tab 项
INSERT INTO `tabs`(`created_at`, `updated_at`, `deleted_at`, `display_name`, `slug`, `location`, `priority`)
VALUES (CURRENT_TIME(), CURRENT_TIME(), NULL, '首页', '', 'home', 0);
INSERT INTO `tabs`(`created_at`, `updated_at`, `deleted_at`, `display_name`, `slug`, `location`, `priority`)
VALUES (CURRENT_TIME(), CURRENT_TIME(), NULL, '清单', '', 'checklist', 1);
INSERT INTO `tabs`(`created_at`, `updated_at`, `deleted_at`, `display_name`, `slug`, `location`, `priority`)
VALUES (CURRENT_TIME(), CURRENT_TIME(), NULL, '我', '', 'user', 2);
INSERT INTO `tabs`(`created_at`, `updated_at`, `deleted_at`, `display_name`, `slug`, `location`, `priority`)
VALUES (CURRENT_TIME(), CURRENT_TIME(), NULL, '今日', '', 'metto', 3);