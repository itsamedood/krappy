from enum import Enum


class Intent(Enum):
  ALL = "All"
  AUTO_MODERATION_CONFIGURATION = "AutoModerationConfiguration"
  AUTO_MODERATION_EXECUTION = "AutoModerationExecution"
  DIRECT_MESSAGE_REACTIONS = "DirectMessageReactions"
  DIRECT_MESSAGE_TYPING = "DirectMessageTyping"
  DIRECT_MESSAGES = "DirectMessages"
  GUILD_EMOJIS_AND_STICKERS = "GuildEmojisAndStickers"
  GUILD_INTEGRATIONS = "GuildIntegrations"
  GUILD_INVITES = "GuildInvites"
  GUILD_MEMBERS = "GuildMembers"
  GUILD_MESSAGE_REACTIONS = "GuildMessageReactions"
  GUILD_MESSAGE_TYPING = "GuildMessageTyping"
  GUILD_MESSAGES = "GuildMessages"
  GUILD_MODERATION = "GuildModeration"
  GUILD_PRESENCES = "GuildPresences"
  GUILD_SCHEDULED_EVENTS = "GuildScheduledEvents"
  GUILD_VOICE_STATES = "GuildVoiceStates"
  GUILD_WEBHOOKS = "GuildWebhooks"
  GUILDS = "Guilds"
  MESSAGE_CONTENT = "MessageContent"


class Partial(Enum):
  ALL = "All"
  CHANNEL = "Channel"
  GUILD_MEMBER = "GuildMember"
  GUILD_SCHEDULED_EVENT = "GuildScheduledEvent"
  MESSAGE = "Message"
  REACTION = "Reaction"
  THREAD_MEMBER = "ThreadMember"
  USER = "User"
